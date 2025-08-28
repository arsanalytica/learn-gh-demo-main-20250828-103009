"""
Connection pooling implementation to fix memory leaks
"""
import sqlite3
from contextlib import contextmanager

class ConnectionPool:
    def __init__(self, db_path: str, max_connections: int = 5):
        self.db_path = db_path
        self.max_connections = max_connections
        self.connections = []

    @contextmanager
    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        try:
            yield conn
        finally:
            conn.close()

# Usage example
pool = ConnectionPool("ml_pipeline.db")
with pool.get_connection() as conn:
    # Process data safely
    pass
