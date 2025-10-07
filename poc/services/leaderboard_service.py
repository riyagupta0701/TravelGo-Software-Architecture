import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask, jsonify
from events import event_bus

app = Flask(__name__)
leaderboard = {}

def handle_new_post(post):
    user_id = post["user_id"]
    leaderboard[user_id] = leaderboard.get(user_id, 0) + 10

event_bus.subscribe("post_created", handle_new_post)

@app.route("/leaderboard", methods=["GET"])
def get_leaderboard():
    sorted_lb = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    return jsonify([{"user_id": uid, "points": pts} for uid, pts in sorted_lb])

if __name__ == "__main__":
    app.run(port=5003)
