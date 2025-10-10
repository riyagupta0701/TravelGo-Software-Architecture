from flask import Flask, render_template, request, redirect, url_for
import requests
import os

template_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'templates')
app = Flask(__name__, template_folder=template_dir)

API_GATEWAY = os.getenv("API_GATEWAY_URL", "http://127.0.0.1:5000")

@app.route("/")
def home():
    attractions = requests.get(f"{API_GATEWAY}/map").json()
    return render_template("index.html", attractions=attractions)

@app.route("/posts", methods=["GET", "POST"])
def posts():
    if request.method == "POST":
        user_id = request.form["user_id"]
        attraction = request.form["attraction"]
        content = request.form["content"]
        requests.post(f"{API_GATEWAY}/posts", json={
            "user_id": int(user_id),
            "attraction": attraction,
            "content": content
        })
        return redirect(url_for("posts"))
    posts = requests.get(f"{API_GATEWAY}/posts").json()
    return render_template("posts.html", posts=posts)

@app.route("/leaderboard")
def leaderboard():
    leaderboard_data = requests.get(f"{API_GATEWAY}/leaderboard").json()
    return render_template("leaderboard.html", leaderboard=leaderboard_data)

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_id = request.form["user_id"]
        message = request.form["message"]
        requests.post(f"{API_GATEWAY}/chat", json={"user_id": int(user_id), "message": message})
        return redirect(url_for("chat"))
    messages = requests.get(f"{API_GATEWAY}/chat").json()
    return render_template("chat.html", messages=messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5008)