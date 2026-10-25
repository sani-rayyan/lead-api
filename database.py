import sqlite3
from contextlib import contextmanager


@contextmanager
def get_db():
    conn = sqlite3.connect("leads.db")
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db():
    with get_db() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS leads(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       email TEXT NOT NULL,
                       phone TEXT,
                       service TEXT,
                       status TEXT DEFAULT 'new',
                       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")




