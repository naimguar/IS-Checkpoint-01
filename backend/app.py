import os
import psycopg2
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def get_db_connection():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        port=int(os.environ.get("DB_PORT", 5432)),
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )


@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/api/team")
def team():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT nombre, apellido, legajo, feature, servicio, estado FROM members")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    members = [
        {
            "nombre": row[0],
            "apellido": row[1],
            "legajo": row[2],
            "feature": row[3],
            "servicio": row[4],
            "estado": row[5],
        }
        for row in rows
    ]
    return jsonify(members)


@app.route("/api/info")
def info():
    return jsonify({
        "service": "backend",
        "version": "1.0.0",
        "description": "API REST para TeamBoard — IS-2026 Checkpoint 01",
        "endpoints": ["/api/health", "/api/team", "/api/info"],
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
