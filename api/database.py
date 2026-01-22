import sqlite3
from pathlib import Path

DB_PATH = Path("/data/monitor.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cpu_percent REAL,
            memory_percent REAL,
            disk_percent REAL,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()