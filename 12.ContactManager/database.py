import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("./contact.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contact(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                number TEXT NOT NULL
            )
        """)

    def add_item(self, title: str, number: str):
        self.cursor.execute("""
            INSERT INTO contact (title, number) VALUES (?, ?)
        """, (title, number))
        self.commit()

    def fetch(self):
        self.cursor.execute("SELECT * FROM contact")
        return self.cursor.fetchall()

    def delete(self, uid: int):
        self.cursor.execute("DELETE FROM contact WHERE id = ?", (uid,))
        self.commit()

    def get(self, uid: int):
        self.cursor.execute("SELECT * FROM contact WHERE id = ?", (uid,))
        return self.cursor.fetchone()

    def update(self, uid: int, title: str, number: str):
        self.cursor.execute("""
            UPDATE contact SET title=?, number=? WHERE id=?
        """, (title, number, uid))

    def commit(self):
        self.conn.commit()

    def __del__(self):
        self.cursor.close()
        self.conn.close()
