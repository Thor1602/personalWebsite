import sqlite3
from sqlite3 import Error

class User:
    def __init__(self, username_arg, password_arg, remember_me_arg):
        self.username = username_arg
        self.password = password_arg
        self.remember_me = remember_me_arg

    def add_user(self):
        try:
            conn = sqlite3.connect("mainsite.db")
            c = conn.cursor()
            c.execute('CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, password TEXT NOT NULL, remember_me INTEGER NOT NULL)')
            c.execute("INSERT INTO user (name, password, remember_me) VALUES (?,?,?)", (self.username, self.password, self.remember_me))
            conn.commit()
        except Error as e:
            print(e)

        finally:
            c.close()
            conn.close()

    def del_user(self, name):
        try:
            conn = sqlite3.connect("mainsite.db")
            c = conn.cursor()
            c.execute('DELETE FROM user WHERE name = ' + name + '')
            conn.commit()
        except Error as e:
            print(e)

        finally:
            c.close()
            conn.close()

    def read_database(self):
        try:
            conn = sqlite3.connect("mainsite.db")
            c = conn.cursor()
            print([x for x in c.execute("SELECT * FROM user")])
        except Error as e:
            print(e)

        finally:
            c.close()
            conn.close()
    def check_user(self):
        try:
            conn = sqlite3.connect("mainsite.db")
            c = conn.cursor()
            c.execute("SELECT * FROM user WHERE name = '" + self.username + "'")
            query = c.fetchone()
            if query == None:
                return False
            else:
                query_list = [x for x in query]
                if query_list[1] == self.username and query_list[2] == self.password:
                    return True
                else:
                    return False

        except Error as e:
            print(e)
        finally:
            c.close()
            conn.close()

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
