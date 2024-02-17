import sqlite3


class SQLighter:

    def __init__(self, database_file):
        """CONNECT BD SAVE CUR"""
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def whid_bd(self, username):
        """CHECK BD username"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `username` = ?", (username,)).fetchall()
            return result

    def add_hid_db(self, username, whid):
        with self.connection:
         return self.cursor.execute("UPDATE `users` SET `whid` = ? WHERE `username` = ?", (whid, username,))

    def close(self):
        self.connection.close()

    