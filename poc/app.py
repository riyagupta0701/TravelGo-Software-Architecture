from flask import Flask, render_template, redirect, url_for, request
from models import db, User, Post

app = Flask(__name__)
app.secret_key = "travelgo_secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///travelgo.db"
db.init_app(app)


@app.before_request
def create_tables():
    db.create_all()
    if not User.query.first():
        db.session.add(User(username="Alice"))
        db.session.commit()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/posts")
def posts():
    posts = Post.query.all()
    return render_template("posts.html", posts=posts)

@app.route("/add_post", methods=["POST"])
def add_post():
    title = request.form["title"]
    desc = request.form["description"]

    user = User.query.get(1)
    new_post = Post(title=title, description=desc, user_id=user.id)
    db.session.add(new_post)
    user.points += 10
    db.session.commit()
    return redirect(url_for("posts"))

@app.route("/leaderboard")
def leaderboard():
    users = User.query.order_by(User.points.desc()).all()
    return render_template("leaderboard.html", users=users)

@app.route("/forum")
def forum():
    return render_template("forum.html")

if __name__ == "__main__":
    app.run(debug=True)
