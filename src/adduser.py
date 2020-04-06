"""
Class to hold the "add user" behaviour.
"""
import sqlite3
import hashlib

def add_user(_user, pwd, _type):
    """
    Add user to USER table via SQL
    """
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute(f'Insert into USER(_user,pass,type) values("{_user}","{pwd}","{_type}");')
    conn.commit()
    conn.close()

with open('users.csv', 'r') as file:
    LINES = file.read().splitlines()

for users in LINES:
    (_user, _type) = users.split(',')
    print(_user)
    print(_type)
    add_user(_user, hashlib.md5(_user.encode()).hexdigest(), _type)
