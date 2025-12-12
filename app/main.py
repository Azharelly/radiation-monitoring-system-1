import os
from flask import Flask, request, jsonify
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
# Rutas API
# ------------------------

@app.route("/")
def home():
    return jsonify({"status": "Radiation Monitoring API is running"}), 200


# Ahora estos endpoints siguen mock hasta que conectemos la DB
@app.route("/logs", methods=["GET"])
def get_logs():
    return jsonify({"info": "Database connection not enabled yet"}), 200


@app.route("/logs", methods=["POST"])
def create_log():
    data = request.get_json()
    return jsonify({
        "message": "Log received (DB connection not enabled yet)",
        "data": data
    }), 201


# Ejecutar localmente
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
