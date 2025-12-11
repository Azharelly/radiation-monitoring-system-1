from flask import Flask, request, jsonify

app = Flask(__name__)

# Route raíz: confirma que la app está viva
@app.route("/")
def home():
    return jsonify({"status": "Radiation Monitoring API is running"}), 200

# GET /logs — ahora mismo devuelve datos falsos (mock)
@app.route("/logs", methods=["GET"])
def get_logs():
    sample_data = [
        {"id": 1, "sensor_id": "A1", "radiation_level": 3.5, "timestamp": "2025-01-01 12:00:00"},
        {"id": 2, "sensor_id": "B2", "radiation_level": 4.1, "timestamp": "2025-01-01 12:05:00"}
    ]
    return jsonify(sample_data), 200

# POST /logs — ahora mismo solo recibe datos y devuelve OK
@app.route("/logs", methods=["POST"])
def create_log():
    data = request.get_json()
    return jsonify({
        "message": "Log received (DB not connected yet)",
        "data": data
    }), 201

# Run locally (Compute Engine will run through Docker)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
