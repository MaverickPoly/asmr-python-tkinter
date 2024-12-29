import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("todos.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed INTEGER DEFAULT 0
            )
        """)

    def add(self, title: str, completed: int):
        self.cur.execute("""
            INSERT INTO todos (title, completed) VALUES (?, ?)
        """, (title, completed))
        self.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM todos")
        results = self.cur.fetchall()
        return results

    def fetch_completed(self):
        self.cur.execute("SELECT * FROM todos WHERE completed = 1")
        return self.cur.fetchall()

    def fetch_uncompleted(self):
        self.cur.execute("SELECT * FROM todos WHERE completed = 0")
        return self.cur.fetchall()

    def delete(self, id: int):
        self.cur.execute("DELETE FROM todos WHERE id = ?", (id,))
        self.commit()

    def get(self, id: int):
        self.cur.execute("SELECT * FROM todos WHERE id = ?", (id,))
        return self.cur.fetchone()

    def update(self, id: int, title: str, completed: int):
        self.cur.execute("""
            UPDATE todos SET title=?, completed=? WHERE id=?
        """, (title, completed, id))
        self.commit()

    def commit(self):
        self.conn.commit()

    def __del__(self):
        self.cur.close()
        self.conn.close()


# database = Database()
# database.add("Groceries", 1)
# database.delete(id=1)
# print(database.get(3))
# database.update(3, "Buy Groceries", 0)
# print(database.fetch())



