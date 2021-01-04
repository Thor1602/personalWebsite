import dbHelper

user = dbHelper.User('user', 'password', True)
user.check_connection()