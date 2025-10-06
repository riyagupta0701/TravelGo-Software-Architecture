from flask import Flask, jsonify

app = Flask(__name__)

attractions = [
    {"id": 1, "name": "Eiffel Tower", "lat": 48.8566, "lng": 2.3522, "description": "Famous tower."},
    {"id": 2, "name": "Statue of Liberty", "lat": 40.7128, "lng": -74.0060, "description": "Famous statue."},
    {"id": 3, "name": "Van Gogh Museum", "lat": 52.3584, "lng": 4.8811, "description": "Famous art museum."},
    {"id": 4, "name": "Shibuya Crossing", "lat": 35.6895, "lng": 139.6917, "description": "Famous crossing."}
]

@app.route("/map", methods=["GET"])
def get_map():
    return jsonify(attractions)
