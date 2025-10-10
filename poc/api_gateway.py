from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

USER_SERVICE = os.getenv("USER_SERVICE_URL", "http://127.0.0.1:5001")
POST_SERVICE = os.getenv("POST_SERVICE_URL", "http://127.0.0.1:5002")
LEADERBOARD_SERVICE = os.getenv("LEADERBOARD_SERVICE_URL", "http://127.0.0.1:5003")
CHAT_SERVICE = os.getenv("CHAT_SERVICE_URL", "http://127.0.0.1:5004")
MAP_SERVICE = os.getenv("MAP_SERVICE_URL", "http://127.0.0.1:5005")

@app.route("/users", methods=["POST"])
def create_user():
    resp = requests.post(f"{USER_SERVICE}/users", json=request.json)
    return jsonify(resp.json()), resp.status_code

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    resp = requests.get(f"{USER_SERVICE}/users/{user_id}")
    return jsonify(resp.json()), resp.status_code

@app.route("/posts", methods=["POST"])
def create_post():
    resp = requests.post(f"{POST_SERVICE}/posts", json=request.json)
    return jsonify(resp.json()), resp.status_code

@app.route("/posts", methods=["GET"])
def get_posts():
    resp = requests.get(f"{POST_SERVICE}/posts")
    return jsonify(resp.json()), resp.status_code

@app.route("/leaderboard", methods=["GET"])
def get_leaderboard():
    resp = requests.get(f"{LEADERBOARD_SERVICE}/leaderboard")
    return jsonify(resp.json()), resp.status_code

@app.route("/chat", methods=["POST"])
def send_chat():
    resp = requests.post(f"{CHAT_SERVICE}/chat", json=request.json)
    return jsonify(resp.json()), resp.status_code

@app.route("/chat", methods=["GET"])
def get_chat():
    resp = requests.get(f"{CHAT_SERVICE}/chat")
    return jsonify(resp.json()), resp.status_code

@app.route("/map", methods=["GET"])
def get_map():
    resp = requests.get(f"{MAP_SERVICE}/map")
    return jsonify(resp.json()), resp.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)