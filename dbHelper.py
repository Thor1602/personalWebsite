import sqlite3
from sqlite3 import Error

class Main:
    def execute_query(self, query_list, commit=False, fetchAll=False, fetchOne=False):
        try:
            conn = sqlite3.connect("mainsite.db")
            c = conn.cursor()
            result = None
            if type(query_list) == str:
                c.execute(query_list)
            else:
                for query in query_list:
                    c.execute(query)
            if commit:
                conn.commit()
            if fetchAll:
                result = [row for row in c.fetchall()]
            if fetchOne:
                result = c.fetchone()
        except Error as e:
            print(e)
        finally:
            c.close()
            conn.close()
            return result

    def read_database(self, db_name):
        data = self.execute_query(query_list="SELECT * FROM " + db_name + "", fetchAll=True)
        print(data)

class User(Main):
    def __init__(self, username_arg, password_arg, remember_me_arg):
        self.username = username_arg
        self.password = password_arg
        self.remember_me = remember_me_arg

    def to_string(self):
        return self.username + ", " + self.password + ", " + str(self.remember_me)+ "."

    def add_user(self):
        query1 ="""CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, password TEXT NOT NULL, remember_me INTEGER NOT NULL)"""
        query2 = "INSERT INTO user (name, password, remember_me) VALUES (?,?,?)", (self.username, self.password, self.remember_me)
        query_list = [query1, query2]
        self.execute_query(query2, commit=True)

    def del_user(self, name):
        self.execute_query(query_list='DELETE FROM user WHERE name = ' + name + '', commit=True)

    def check_user(self):
        query = "SELECT * FROM user WHERE name = '" + self.username + "'"
        exec_query = self.execute_query(query_list=query, fetchOne=True)
        if exec_query == None:
            return False
        else:
            query_list = [x for x in exec_query]
            if query_list[1] == self.username and query_list[2] == self.password:
                return True
            else:
                return False

class Blog(Main):
    def add_entry(self, title, description, paragraphlist, listImageID):
        query1 ="""CREATE TABLE IF NOT EXISTS blogs (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        date DATE NOT NULL,
        title TEXT NOT NULL, 
        description TEXT NOT NULL, 
        paragraph1 TEXT NOT NULL,
        paragraph2 TEXT NOT NULL,
        paragraph3 TEXT NOT NULL,
        paragraph4 TEXT NOT NULL,
        paragraph5 TEXT NOT NULL,
        paragraph6 TEXT NOT NULL,
        paragraph7 TEXT NOT NULL,
        paragraph8 TEXT NOT NULL,
        paragraph9 TEXT NOT NULL,
        paragraph10 TEXT NOT NULL,
        paragraph11 TEXT NOT NULL,
        paragraph12 TEXT NOT NULL,
        listImageID TEXT NOT NULL)"""
        query2 = "INSERT INTO user (name, password, remember_me) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", ()
        query_list = [query1, query2]
        self.execute_query(query_list=query_list, commit=True)

    def remove_entry(self):
        pass
    def update_entry(self):
        pass


class Project(Main):
    pass

class Tutorial(Main):
    pass

class Settings(Main):
    pass

class MediaUpload(Main):
    table_name = "media_upload"
    def add_entry(self, image_id, url):
        query1 = """"""
        query2 = ""
        query_list = [query1, query2]
        self.execute_query(query_list=query_list, commit=True)

    def remove_entry(self, image_id):
        self.execute_query(query_list='DELETE FROM ' + self.table_name + ' WHERE image_id = ' + image_id + '', commit=True)
    def update_entry(self, image_id='', url=''):
        query = "UPDATE table SET column_1 = new_value_1, column_2 = new_value_2 WHERE search_condition"
        self.execute_query(query_list='UPDATE ' + self.table_name + ' SET image_id = ' + image_id + '', commit=True)



class Comment(Main):
    pass

class Info(Main):
    pass
