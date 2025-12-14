import os
from flask import Flask, request, jsonify, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# ------------------------
# Helper: conectar a MySQL
# ------------------------
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return connection
    except Error as e:
        print("Database connection error:", e)
        return None

# ------------------------
# Health check (API)
# ------------------------
@app.route("/")
def health():
    return {"status": "Radiation Monitoring API is running"}

# ------------------------
# Frontend pages
# ------------------------
@app.route("/log", methods=["GET"])
def log_page():
    return render_template("log.html")

@app.route("/history", methods=["GET"])
def history_page():
    return render_template("history.html")

# ------------------------
# API endpoints
# ------------------------
@app.route("/api/logs", methods=["POST"])
def create_log():
    data = request.form or request.get_json()

    radiation_level = data.get("radiation_level")
    sensor_id = data.get("sensor_id")

    if not radiation_level or not sensor_id:
        return jsonify({"error": "Missing data"}), 400

    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        cursor = connection.cursor()
        query = """
            INSERT INTO radiation_logs (sensor_id, radiation_level)
            VALUES (%s, %s)
        """
        cursor.execute(query, (sensor_id, radiation_level))
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Log saved"}), 201
    except Error as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/logs", methods=["GET"])
def get_logs():
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM radiation_logs ORDER BY timestamp DESC")
    logs = cursor.fetchall()
    cursor.close()
    connection.close()

    return jsonify(logs), 200

# ------------------------
# Run locally
# ------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
