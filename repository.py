import sqlite3

class Repository:
    def __init__(self,table):
        self.table = table 
        self.database = self.table + ".db" 
        self.make()

    def make(self):
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {self.table} " +
                "(title TEXT PRIMARY KEY, artist TEXT, file TEXT)"
            )
            connection.commit()

    def clear(self):
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"DELETE FROM {self.table}" 
            )
            connection.commit()

    def insert(self,js):
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"INSERT INTO {self.table} (title,artist,file) VALUES (?,?,?)",
                (js["title"],js["artist"],js["file"])
            )
            connection.commit()
            return cursor.rowcount

    def update(self, js):
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"UPDATE {self.table} SET artist=?, file=? WHERE title=?",
                (js["artist"], js["file"], js["title"])
            )
            connection.commit()
            return cursor.rowcount


    def lookup(self,title):
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"SELECT title, artist, file FROM {self.table} WHERE title=?",
                (title,)
            )
            row = cursor.fetchone()
            if row:
                return {"title":row[0],"artist":row[1], "file":row[2]}
            else:
                return None

    def delete(self,title):
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"DELETE FROM {self.table} WHERE title=?",
                (title,)
            )
            connection.commit()
            return cursor.rowcount

    def list(self):
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"SELECT title, artist, file FROM {self.table}"
            )
            rows = cursor.fetchall()
            return [{"title":row[0],"artist":row[1],"file":row[2]} for row in rows]
