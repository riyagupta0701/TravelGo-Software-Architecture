import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask, request, jsonify
from events import event_bus

app = Flask(__name__)
messages = []

def handle_new_post(post):
    msg = f"User {post['user_id']} shared a new experience: {post['content']}"
    messages.append(msg)

event_bus.subscribe("post_created", handle_new_post)

@app.route("/chat", methods=["POST"])
def send_message():
    data = request.json
    messages.append(f"User {data['user_id']}: {data['message']}")
    return jsonify({"status": "ok"}), 201

@app.route("/chat", methods=["GET"])
def get_messages():
    return jsonify(messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5004)