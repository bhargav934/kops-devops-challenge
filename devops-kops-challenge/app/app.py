from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "apppassword"),
        database=os.getenv("DB_NAME", "appdb")
    )


@app.route("/")
def home():
    return "DevOps Kops Challenge API is running"


@app.route("/health")
def health():
    return {"status": "healthy"}


@app.route("/users")
def users():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT id, name FROM users")
    users = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(users)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
