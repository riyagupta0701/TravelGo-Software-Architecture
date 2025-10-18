import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask, jsonify
from events import event_bus
import threading
from confluent_kafka import Consumer, KafkaError, KafkaException
import json

app = Flask(__name__)
leaderboard = {}
running = True

conf = {'bootstrap.servers': 'kafka:9092',
        'group.id': 'posts',
        'auto.offset.reset': 'earliest'}
consumer = Consumer(conf)

def handle_new_post(post):
    user_id = post["user_id"]
    leaderboard[user_id] = leaderboard.get(user_id, 0) + 10

def process(message):
    try:
        data = json.loads(message.value().decode("utf-8"))
        handle_new_post(data)
    except Exception as exception:
        print('Message not processed: ', exception)

def consume():
    consumer.subscribe(['new_post'])
    try:
        while running:
            message = consumer.poll(timeout=1.0)
            if message is None: 
                continue
            if message.error():
                if message.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    raise KafkaException(message.error())
            else:
                process(message)
    except Exception as exception:
        print('Consume error: ', exception)
    finally:
        consumer.close()

@app.route("/leaderboard", methods=["GET"])
def get_leaderboard():
    sorted_lb = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    return jsonify([{"user_id": uid, "points": pts} for uid, pts in sorted_lb])

if __name__ == "__main__":
    consumer_thread = threading.Thread(target=consume, daemon=True)
    consumer_thread.start()
    app.run(host="0.0.0.0",port=5003)
