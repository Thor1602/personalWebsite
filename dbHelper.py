import sqlite3
from sqlite3 import Error

class User:
    def __init__(self, username_arg, password_arg, remember_me_arg):
        self.username = username_arg
        self.password = password_arg
        self.remember_me = remember_me_arg

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect("mainsite.db")
            return conn
        except Error as e:
            print(e)
        return conn

    def add_user(self):
        try:
            conn = sqlite3.connect("mainsite.db")
            c = conn.cursor()
            c.execute(""" CREATE TABLE IF NOT EXISTS user (
                                                    id integer PRIMARY KEY AUTOINCREMENT,
                                                    name text NOT NULL,
                                                    password text NOT NULL,
                                                    remember_me boolean NOT NULL
                                                ); """)
            c.execute("""INSERT INTO USER(
                                
            );""")
        except Error as e:
            print(e)

        finally:
            c.close()
            conn.close()


    def del_user(self):
        pass

class Blog:
    pass

class Project:
    pass

class Tutorial:
    pass

class Comment:
    pass

class Info:
    pass
