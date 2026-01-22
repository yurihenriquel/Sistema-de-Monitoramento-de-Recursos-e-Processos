from flask import Blueprint, request, jsonify
from api.database import get_connection
from datetime import datetime

metrics_bp = Blueprint("metrics", __name__)


@metrics_bp.route("/metrics", methods=["POST"])
def create_metric():
    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO metrics (cpu_percent, memory_percent, disk_percent, created_at)
        VALUES (?, ?, ?, ?)
    """, (
        data.get("cpu_percent"),
        data.get("memory_percent"),
        data.get("disk_percent"),
        datetime.utcnow().isoformat()
    ))

    conn.commit()
    conn.close()

    return jsonify({"status": "ok"}), 201


@metrics_bp.route("/metrics", methods=["GET"])
def list_metrics():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT cpu_percent, memory_percent, disk_percent, created_at
        FROM metrics
        ORDER BY created_at DESC
        LIMIT 50
    """)

    rows = cursor.fetchall()
    conn.close()

    return jsonify([dict(row) for row in rows])