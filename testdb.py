import dbHelper

user1 = dbHelper.User('thorben1602', "WPvX4NNn2rRTg56QW52V", 1)
user2 = dbHelper.User('sumin2502', "vX4N26QW5%%rRT2VWPng", 1)
user2.add_user()
user1.read_database('user')