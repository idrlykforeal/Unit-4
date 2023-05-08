import os

from flask import Flask, render_template, request, make_response, redirect, url_for
from werkzeug.utils import secure_filename

from MyLib import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

create_database()

@app.route('/logout')
def logout():
    response = make_response(render_template('home.html'))
    response.set_cookie('user_id', '', expires=0)
    response.set_cookie('is_admin', '', expires=0)
    return response

@app.route('/login', methods=['POST', 'GET'])
def login():
    msg = ""
    if request.method == "POST":
        username = request.form['username']
        passwd=request.form['passwd']
        db = database_worker("ikou_network.db")
        user = db.search(f"Select * from users where username = '{username}'")
        if user:
            user=user[0] #because search function returns a list of users (in this case only 1)
            user_id = user[0] #because search function returns a list
            registered_password = user[3]
            if check_pswd(hashed_pswd=registered_password, user_pswd=passwd):
                response = make_response(render_template('home.html'))
                response.set_cookie('user_id', f"{user_id}")#cookie is a string
                response.set_cookie('is_admin', f"{user[4]}")
                return response
            else:
                msg = "password does not match"
        else:
            msg = "user does not exist"
    return render_template("login.html", message=msg)

@app.route('/register', methods=['POST', 'GET'])
def register():
    success=""
    msg=""
    if request.method == "POST":

        msg= ""
        success = ""

        email = request.form['email']
        username=request.form['username']
        passwd=request.form['passwd']
        confirm_passwd=request.form['confirm_passwd']

        # validate username
        msg += validate_username(username)

        # validate email
        msg += validate_email(email)

        # validate password
        msg += validate_password(passwd, confirm_passwd)

        if msg == "":
            hashed_password = encrypt_pswd(passwd)
            add_user(email=email, username=username, password=hashed_password)
            success="You have successfully registered!"
            render_template('login.html')
    return render_template("register.html", message=msg, success=success)

@app.route('/planned_trips', methods=['POST', 'GET'])
def planned_trips():

    db = database_worker("ikou_network.db")
    admin_posts = db.search("SELECT * FROM admin_posts")

    user_info=None
    # if the cookie exists,
    if request.cookies.get('user_id'):
        userid = request.cookies.get('user_id')
        user_info = db.search(f"SELECT * FROM users WHERE id = '{userid}'")[0]

    msg = ""

    if request.method == "POST":

        # get post information from the form
        post_title = request.form['title']
        post_content = request.form['content']
        post_image = request.files['photo']

        msg += check_content(post_title)
        msg = check_content(post_content)

        if post_image.filename == "":
            msg += "Please select a photo"


        if msg == "":

            filename = secure_filename(post_image.filename)
            post_image.save(os.path.join(app.root_path, 'static/photos', filename))

            # add post to database

            add_admin_post(username=user_info[2] ,user_id=userid, title=post_title, content=post_content, photo_location=filename)


            return redirect(url_for("planned_trips"))


    return render_template('planned_trips.html', msg=msg, admin_posts=admin_posts, user_info=user_info)

@app.route('/posts', methods=['POST', 'GET'])
def posts():
    # get cookies

    db = database_worker("ikou_network.db")
    username=None
    user_id=None
    if request.cookies.get('user_id'):
        user_id = request.cookies.get('user_id')
        # search user information from database from the user id
        user = db.search(f"SELECT * FROM users WHERE id = '{user_id}'")
        user_info = user[0]
        username=user_info[2]

    user_posts = db.search("SELECT * FROM posts")
    msg = ""

    if request.method == "POST":

        # get post information from the form
        post_title = request.form['title']
        post_content = request.form['content']
        post_image = request.files['photo']

        msg += check_content(post_title)
        msg = check_content(post_content)

        if post_image.filename == "":
            msg += "Please select a photo"

        if msg == "":

            # getting a secured file name for the image
            filename = secure_filename(post_image.filename)

            # storing image in the static/photos folder with the name
            post_image.save(os.path.join(app.root_path, 'static/photos', filename))

            # add post to database
            add_post(username=username ,user_id=user_id, title=post_title, content=post_content, photo=filename)
            return redirect(url_for("posts"))

    return render_template('posts.html', msg=msg, user_posts=user_posts, user_id=user_id, username=username)


if __name__ == '__main__':
    app.run()
