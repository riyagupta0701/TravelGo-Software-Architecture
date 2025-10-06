from flask import Flask, jsonify

app = Flask(__name__)

attractions = [
    {"id": 1, "name": "Eiffel Tower", "location": "Paris"},
    {"id": 2, "name": "Colosseum", "location": "Rome"},
    {"id": 3, "name": "Van Gogh Museum", "location": "Amsterdam"}
]

@app.route("/map", methods=["GET"])
def get_map():
    return jsonify(attractions)
