from flask import Flask, request, jsonify
from events import event_bus

app = Flask(__name__)
posts = []

@app.route("/posts", methods=["POST"])
def create_post():
    data = request.json
    post_id = len(posts) + 1
    post = {"id": post_id, "user_id": data["user_id"], "content": data["content"]}
    posts.append(post)

    event_bus.publish("post_created", post)

    return jsonify(post), 201

@app.route("/posts", methods=["GET"])
def list_posts():
    return jsonify(posts)
