import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask, request, jsonify
from confluent_kafka import Producer
import json
import time
app = Flask(__name__)
posts = []

conf = {'bootstrap.servers': 'kafka:9092'}
producer = Producer(conf)
dummy_post = {"id": 0, "user_id": 1, "attraction": "Eiffel Tower", "content": "Great"}
posts.append(dummy_post)

for i in range(10):
    try:
        producer.produce(topic='new_post', value=json.dumps(dummy_post).encode('utf-8'))
        producer.flush()  
        break
    except Exception as e:
        time.sleep(2)

def delivered(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

@app.route("/posts", methods=["POST"])
def create_post():
    data = request.json
    post_id = len(posts) + 1
    post = {"id": post_id, "user_id": data["user_id"], "attraction": data["attraction"], "content": data["content"]}
    posts.append(post)

    producer.produce(topic='new_post', value=json.dumps(post).encode('utf-8'), callback=delivered)
    producer.flush()
    return jsonify(post), 201

@app.route("/posts", methods=["GET"])
def get_posts():
    return jsonify(posts)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5002)