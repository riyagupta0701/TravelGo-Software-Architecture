import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask, request, jsonify

app = Flask(__name__)
users = {}

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    user_id = len(users) + 1
    users[user_id] = {"id": user_id, "name": data["name"], "points": 0}
    return jsonify(users[user_id]), 201

@app.route("/users/{user_id}", methods=["GET"])
def get_user(user_id):
    return jsonify(users.get(user_id, {}))

if __name__ == "__main__":
    app.run(port=5001)