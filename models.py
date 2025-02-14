import sqlite3
from config import DATABASE

def init_db():
    """Initialize the SQLite database and create tables."""
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS models (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        version TEXT,
                        accuracy REAL,
                        file_path TEXT)''')
        conn.commit()

def insert_model(name, version, accuracy, file_path):
    """Insert a new model's metadata into the database."""
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO models (name, version, accuracy, file_path) VALUES (?, ?, ?, ?)",
                  (name, version, accuracy, file_path))
        conn.commit()

def get_all_models():
    """Retrieve all models' metadata from the database."""
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM models")
        return c.fetchall()

def get_model_by_name(name):
    """Retrieve a model's metadata by its name."""
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM models WHERE name = ?", (name,))
        return c.fetchone()
