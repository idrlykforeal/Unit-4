import datetime
import sqlite3
from datetime import date


# code for database handler
class database_worker:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()
# password encryption



from passlib.hash import sha256_crypt

# create an object of the class CrypContext

hasher = sha256_crypt.using(rounds= 30000)

def encrypt_pswd(user_password):
    return hasher.encrypt(user_password)

def check_pswd(hashed_pswd, user_pswd):
    return hasher.verify(user_pswd, hashed_pswd)

def create_database():
    db = database_worker("ikou_network.db")
    query_user="""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY, 
        email TEXT, 
        username TEXT,
        password TEXT,
        is_admin BOOLEAN
        )"""
    query_post = """CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY, 
        title VARCHAR(100),
        content TEXT,
        user_id INTEGER, 
        FOREIGN KEY (user_id) REFERENCES users(id) on delete cascade
        )"""
    query_admin_post = """CREATE TABLE IF NOT EXISTS admin_posts (
            id INTEGER PRIMARY KEY, 
            title VARCHAR(100),
            content TEXT,
            user_id INTEGER, 
            FOREIGN KEY (user_id) REFERENCES users(id) on delete cascade
            )"""

    db.run_save(query_user)
    db.run_save(query_post)
    db.run_save(query_admin_post)
    db.close()

admin_emails= ["2024.ziqian.ni@uwcisak.jp","2024.yining.zhang@uwcisak.jp","2024.vera.hoffman@uwcisak.jp"]

def add_user(email, username, password):
    db = database_worker("ikou_network.db")
    is_admin = False
    for i in admin_emails:
        if email == i:
            is_admin = True
    query = f"INSERT INTO users (email, username, password, is_admin) VALUES ('{email}', '{username}','{password}', '{is_admin}')"
    db.run_save(query)
    db.close()


def add_post(title, content, username, user_id, photo):
    db = database_worker("ikou_network.db")
    # get current date
    date_today = date.today()
    query = f"INSERT INTO posts (title, content, username, user_id, date, photo_data) VALUES ('{title}', '{content}', '{username}', '{user_id}', '{date_today}', '{photo}')"
    db.run_save(query)
    db.close()

def add_admin_post(title, content, username, user_id, photo_location):
    db = database_worker("ikou_network.db")
    # get current date
    date_today = date.today()
    query = f"INSERT INTO admin_posts (title, content, date, photo, username, user_id) VALUES ('{title}', '{content}', '{date_today}', '{photo_location}', '{username}', '{user_id}')"
    db.run_save(query)
    db.close()

# validation of email
def validate_email(email):
    msg=""
    if "@" not in email:
        msg = "email must contain @. "
    if " " in email:
        msg = "email must not contain space."
    #check if email already registered
    db = database_worker("ikou_network.db")
    query = f"SELECT * FROM users WHERE email = '{email}'"
    result = db.search(query)
    if len(result) != 0:
        msg = "Email already registered. "
    return msg
# validation of password: length and match
def validate_password(password, password_confirm):
    msg=""
    if len(password) < 8:
        msg = "Password must be at least 8 characters. "
    if password != password_confirm:
        msg += "Password does not match. "
    return msg

# validation of username: if exists already and space
def validate_username(username):
    msg=""
    db = database_worker("ikou_network.db")
    query = f"SELECT * FROM users WHERE username = '{username}'"
    result = db.search(query)
    if len(result) != 0:
        msg = "Username already exists. "
    #validate: not include space
    if " " in username:
        msg =  "Username should not contain space. "
    return msg

def check_content(content):
    msg=""
    if len(content) == 0:
        msg = "Content cannot be empty. "
    return msg

