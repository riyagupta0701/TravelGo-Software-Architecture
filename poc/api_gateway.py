from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

USER_SERVICE = "http://127.0.0.1:5001"
POST_SERVICE = "http://127.0.0.1:5002"
LEADERBOARD_SERVICE = "http://127.0.0.1:5003"
CHAT_SERVICE = "http://127.0.0.1:5004"
MAP_SERVICE = "http://127.0.0.1:5005"

@app.route("/users", methods=["POST"])
def create_user():
    return requests.post(f"{USER_SERVICE}/users", json=request.json).json()

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return requests.get(f"{USER_SERVICE}/users/{user_id}").json()

@app.route("/posts", methods=["POST"])
def create_post():
    return requests.post(f"{POST_SERVICE}/posts", json=request.json).json()

@app.route("/posts", methods=["GET"])
def list_posts():
    return requests.get(f"{POST_SERVICE}/posts").json()

@app.route("/leaderboard", methods=["GET"])
def get_leaderboard():
    return requests.get(f"{LEADERBOARD_SERVICE}/leaderboard").json()

@app.route("/chat", methods=["POST"])
def send_chat():
    return requests.post(f"{CHAT_SERVICE}/chat", json=request.json).json()

@app.route("/chat", methods=["GET"])
def get_chat():
    return requests.get(f"{CHAT_SERVICE}/chat").json()

@app.route("/map", methods=["GET"])
def get_map():
    return requests.get(f"{MAP_SERVICE}/map").json()
