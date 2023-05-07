# Ikou Network

## Criteria A

### Problem Definition
The problem addressed by the "Project Ikou" CAS group is a lack of a centralized platform for the group to manage project informations. The group has previously tried to use google sheets to organize information, but it did not work out well since it is not secure to edit, and users cannot create their accounts to post. So, now the group wants a platform where everyone can view project introduction, project information, and the future trips that are planned for the project. The group wants viewers to be able to create their own account and share their own travelling experience with photos and blog post content, which all viewers of the website can read. The group also wants to have administrator accounts, where they are the only ones able to update future trip plans with posts. The group also want the website to have a clear organization that displays and guides viewers to each page. 

### Proposed Solution
As part of the CAS group, I interviewed my group mate (Appendix 1), and confirmed that the client(Project Ikou) would like to have a website with Python Flask using the languages of python, HTML, and CSS. The website should have a log in and sign up system, that also assigns the project members as administrators, where user informations are stored in SQLite database. The website allows users to post and administrators to post extra contents, where the title, content, and photos uploaded by the users are stored in another table in the SQLite database. The website fetches data from the database to display the user and administrator posts.


### Rationale for Proposed solution
A website would be the perfect platform because it is one of the most accessible platforms that can run on browsers which all users will be able to have. It also allows all the requirements of Project IKOU: it has post and get requests that allow users to register and login, and create posts. Compared to other alternatives such as applications, websites are way more accessable and light-weighted since they do not need to be installed, and can just run on users' default browsers

Python Flask is a great tool to develop websites because it is simple and flexible. Flask provides a lightweight and modular structure that allows developers to build web applications quickly and easily. With a built-in development server and support for multiple extensions, Python Flask can be used to add functionality to the application. Flask is particularly suitable for small to medium-sized web applications with low to medium traffic, which is what we are aiming for. [^1]


To build up the website, HTML and CSS are the base languages of website development. With HTML, we are able to build the structure and content of the website, and with CSS, we are able to edit the styling and layout. Together, they provide the structure and appearance of websites.

To store user information and post informations, SQLite is a great choice since SQLite is a lightweight, file-based relational database. It is suitable for small to medium-sized web applications. SQLite stores data in a single file, making access, usage, and maintenance simple.

**Design Statement** I will to design and make a web based social media site for a client who is a high school student-led project that is interested promoting local torism. The SNS will be about sharing and viewing Project planned trips and others' trip experiences and is constructed using the software CSS, HTML and Python. It will take 4 weeks to make and will be evaluated according to the criteria A, B, C, D, and E.


### Success Criteria

| no | success criteria                                                                                                                                                                                     | issue tackled                                                                                                                                                                                    |
|----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | the website has a login and registration system, where users will be separated into administrators and regular users, administrators can only be registered with the emails of the CAS group members | The group wants viewers to be able to create their own account, The group also wants to have administrator accounts,                                                                             |
|  2 | the website allows all logged in users to create a post, including title, content, and upload pictures                                                                                               | The group wants viewers to be able to create their own account and share their own travelling experience with photos and blog post content,                                                      |
|  3 | the website has a section for posting planned trips that is protected that is only accessable to administrators                                                                                      | The group also wants to have administrator accounts, where they are the only ones able to update future trip plans with posts.                                                                   |
|  4 | all viewers, no matter logged in or not, are able to view user posts and administrator posts which indludes post title, content, time, and picture                                                   | The group wants a platform where everyone can view project introduction, project information, and the future trips that are planned for the project.  which all viewers of the website can read. |
|  5 | the website includes a top navigation bar that is visible on every page that guides users to each page.                                                                                              | The group also want the website to have a clear organization that displays and guides viewers to each page.                                                                                      |
|  6 | the website displays information about Project Ikou includes project goals, general introduction to the project, and pictures on the home page.                                                      | The group wants a platform where everyone can view project introduction, project information, and the future trips that are planned for the project.                                             |

## Criteria B

Design overview (Criterion B) provides evidence that the product could be further developed.

#### diagrams
- System Diagram.
<img width="1252" alt="image" src="https://user-images.githubusercontent.com/100017195/236354824-3c19ee2b-650b-4030-a5dc-84f192877922.png">

**Fig #** System diagram of Ikou Network

- Flow diagrams for algorithms.
![flow_login](https://user-images.githubusercontent.com/100017195/236600976-197924e9-e8e8-45b4-b83a-5c777c814b3a.jpeg)

**Fig #** Flow diagram for login algorithm

![API flowchart example](https://user-images.githubusercontent.com/100017195/236601032-379bff5e-531a-49d4-b1b9-0ba24570ad3a.jpeg)

**Fig #** Flow diagram for validation of username

![flow_adminposts](https://user-images.githubusercontent.com/100017195/236601041-4a998e3a-5c19-4827-9822-0aa972b000d7.jpeg)

**Fig #** Flow diagram for administrator post algorithm


- Database ER diagram 
<img width="957" alt="image" src="https://user-images.githubusercontent.com/100017195/236351392-7371d4fb-27a7-4472-942f-9990d4e19202.png">

**Fig #** ER diagram for example data entities used

  - example data:
<img width="665" alt="image" src="https://user-images.githubusercontent.com/100017195/236601117-bec92def-ee34-468c-a848-0030c499f9a5.png">

**Fig #** Screenshot example of how the user table is structured

<img width="1144" alt="image" src="https://user-images.githubusercontent.com/100017195/236601254-9f437f14-d618-47a6-9498-08868471ccd4.png">

**Fig #** Screenshot example of how the posts table is structured



**Fig #** Example ER diagram of users and posts. 

- Annotated screen mockups or wireframes.
![wiafram](https://user-images.githubusercontent.com/100017195/236349210-16fc96d9-19c5-4a13-bfbd-4b38059ebc4f.jpg)
**Fig #** Wireframe diagram for Ikou Network.

### Record of Tasks
- template (0 without)
- Includes all 5 stages of the design cycle (plan, design, develop, test, implement)
- Planned action is specific and defined which results in the expected outcome (logical connection)
- Relates to the product proposed in Criterion A (not a record of making some alternative product)
- Should mainly cover the tasks involved in the development of the product
- Updated during the life of the project (think about a daily entries)
- Provides a realistic plan and timeline for managing the solution, including the gathering of necessary information, the development of the product, the - - testing process, and the implementation of the product.

### Design Overview




#### Test Plan
|                     Instruction                    |        Category        |             Input example / code            |                                          Description                                         |                                                                      Expected output                                                                      | Success criteria |
|:--------------------------------------------------:|:----------------------:|:-------------------------------------------:|:--------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------:|
| Test registration-success                          | Unit testing           | Username, email, password, password confirm | register account, input username, email, password, password confirm, all information correct | page refreshes, and displays success message "account successfully created"                                                                               |                1 |
| Test registration-username/email exists            | Unit testing           | Username, email, password, password confirm | input a username/email already used                                                          | if username, email aready used, error displays, saying either username or emal already is registered for an existing account.                             |                1 |
| Test registration-password error                   | Unit testing           | Username, email, password, password confirm | password does not match, or password less than 8 digits                                      |  If the password do not match, error displays. If the password length is less than 8, error displays.                                                     |                1 |
| Test the login                                     | Unit testing           | Username and password                       | enter correct username and password, enter incorrect username or password                    | The user logs in if the username and password is correct. Error message displays when the username is not registered, or when the password does not match |                1 |
| Test registration and login                        | Integrated testing     | Username, email, password, password confirm | register an account, and log in with the correct information                                 | user successfully register an account see a success message, and in log-in successfully log in with the registered account.                               |                1 |
| Test post page viewability/ post-visitor           | Integrated testing     | N/A                                         | user logged out, and visit "user post" page                                                  | user able to view all the posts posted, but unable to post, receive a text saying"please log in to post"                                                  |                4 |
| Test post page viewability/ post- regular user     | Integrated testing     | N/A                                         | user logged in regular accounts, visit "user post" page                                      | user able to view all the posts posted, able to post, a post section visible, user able to enter title, content, upload pictures and post                 | 1,2,4            |
| Test admin post visibility and post-non admin user | Integrated testing     | username, password                          | user either log in to regular account, or not logged in at all. visit page "admin post"      | user able to view all the admin posts, but unable to post admin posts, receive text guide "log in to admin account to post planned trips"                 | 1,3,4            |
| Test admin post visibility and post-admin user     | Integrated testing     | username, password                          | user logged in admin acccounts, visit "admin post"                                           | user able to view all the admin posts, able to post, a post section visible, user able to enter title, content, upload pictures and post                  | 1,3,4            |
| Test posting-no input                              | Unit testing           | title, content, picture upload              | no input for title or content                                                                | error message displays: cotent cannot be empty                                                                                                            |                2 |
| Test posting-no pictures                           | Unit testing           | title, content, picture upload              | no photo uploaded                                                                            | error message displays: please upload picture                                                                                                             |                2 |
| Test posting-success                               | Unit testing           | title, content, picture upload              | title, content not empty, photo uploaded                                                     | page refreshes, form empties, and the new post is updated at the end of the page                                                                          |                2 |
| Home page display                                  | Non-functional testing | N/A                                         | visit home page                                                                              | picture, project introduction, project mission, goas visible on the site                                                                                  |                6 |
| Navigation bar                                     | Unit testing           | N/A                                         | click on each section title                                                                  | when click on each section title, goes to the respective page                                                                                             |                5 |

## Criteria C

## Existing Tools

| Software/Development Tools | Coding Structure Tools          | Libraries      |
|----------------------------|---------------------------------|----------------|
| PyCharm                    | Encryption                      | Flask          |
| Relational databases       | Functions                       | sqlite3        |
| SQLite                     | If statements                   | passlib        |
| Python                     | For loops                       | os             |
| Safari (testing)           |                                 | werkzeug       | 
|                            |                                 | datetime       |

## List of techniques used
1. Get/Post methods
2. For loops
3. If statements
4. Password hashing
5. Interacting with databases
6. Lists
7. Cookies
8. Functions

### Success criteria: Login/registration + Administrator accounts

The first problem encountered in the development process is how to register accounts, specifically how to add users of specific emails to administrator accounts. I broke down the problem with **decomposition** and solved each parts individually to make it work. To realize the separation of regular accounts and admin accounts, I decided to add a column of boolean value to the users table to store if they are administrators when users register. To sovle the problem of determining whether users are administrators or not, with **algorithmic thinking** , I came up with a solution of first creating a list of emails stored in MyLib.py (library code), and I subsequently wrote a general function of adding new users that includes checking whether the user input is any of the emails in the list with the structure of a loop before adding new users to the database. Add user code displayed below:

```.py

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
```

With **pattern recognition** I recognized the frequent usage of adding users and validation within the development of login and registration. So, in my library of code Mylib.py, I wrote functions that help add users (displayed above) and validations that can be called in the main app.py to avoid repetition and improve the efficiency of the code. Example of validating email and password shown below:

```.py
def validate_email(email):
    msg=""
    if "@" not in email:
        msg = "email must contain @."
    if " " in email:
        msg = "email must not contain space."
    #check if email already registered
    db = database_worker("ikou_network.db")
    query = f"SELECT * FROM users WHERE email = '{email}'"
    result = db.search(query)
    if len(result) != 0:
        msg = "Email already registered."
    return msg
# validation of password: length and match
def validate_password(password, password_confirm):
    msg=""
    if len(password) < 8:
        msg = "Password must be at least 8 characters."
    if password != password_confirm:
        msg += "Password does not match"
    return msg
```
In general, the registration process is decomposed and realized in 4 steps: fetch, validate(mentioned above), encrypt, and store. So for the 3rd step, to ensure user security of their password, I employed a sha256 hash into the entered password, and then stored the password in to the database. The general code of the process of registration can be seen as below:

```.py
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
        msg =validate_password(passwd, confirm_passwd)

        if msg == "":
            hashed_password = encrypt_pswd(passwd)
            add_user(email=email, username=username, password=hashed_password)
            success="You have successfully registered!"
            render_template('login.html')
```

### Success criteria: Posting pictures

The most difficult part of my second success criteria is that it requires the website to be able to let users upload the pictures, and show the pictures in posts. 

I broke down the problem into 2 main setps: upload, and fetching the photo for displaying the post (**decomposition**) and generated general flow diagrams to help me understand the general process (**algorithmic thinking, abstraction**) (View Fig. xxx from Criteria B)

For uploading the pictures, 2 sub-steps are identified: storing the photo into a sub folder under static, and also storing the name of the photo to the respective column of the database, details shown in code below:

```.py
# getting a secured file name for the image
            filename = secure_filename(post_image.filename)
            
            # storing image in the static/photos folder with the name
            post_image.save(os.path.join(app.root_path, 'static/photos', filename))

            # add post to database
            add_post(username=username ,user_id=user_id, title=post_title, content=post_content, photo=filename)
```

To fetch the images with all information (title, content) of the posts to display the posts in html, I first used **algorithmic thinking** , displaying all posts one by one in a loop. For the display of the photo, I first fetched the filename, and put it in a structured image directory: /static/photos, so that they fetch the photo file that has the same name stored in the database. (**abstraction**)

```.html
{% for post in user_posts %}
        <div class="row">
            <div class="card">
              <h3>{{ post [1] }}</h3>
              <h5>user id:{{ post [4] }}</h5>
                <h5> username: {{ post [3] }}</h5>
                <h5>date: {{ post [5] }}</h5>
                {% if post[6] %}
                <img src="/static/photos/{{ post [6] }}" alt="post image">
                {% endif %}
              <p>{{ post [2] }}</p>
            </div>
        </div>
    {% endfor %}
```


### Success criteria: Protected administrator content

My critera 3 requires there to be a form section for posting planned trips to be only accessable to administrator accounts. 

I decomposed the problem into: fetch current user status and information with cookies, determining whether to diplay or not. (**decomposition**)

First, user information from the cookies can determine they are logged into administrator accounts, information stored in user_info. Python code in detail below:

```.py
    if request.cookies.get('user_id'):
        userid = request.cookies.get('user_id')
        user_info = db.search(f"SELECT * FROM users WHERE id = '{userid}'")[0]
```

I then return user_info to the html template of planned_trips.html, and used a "if" structure (**algorithmic thinking**) to separate the display of the content. HTML code in detail below: 

```.html
{% if user_info[4] == "True" %}
        {% if msg %}
        <p class = 'error_message'>{{ msg }}</p>
        {% endif %}
        <form method="post" enctype="multipart/form-data" class="form">
            <h3>Hi {{ user_info[2] }}, post a new planned trip! </h3>
            <input type="text" name="title" placeholder="Title"><br>
            <textarea name="content" placeholder="Content"></textarea><br>
            <input type="file" id="photo" name="photo">

            <input type="submit" value="Post">
        </form>
    {% else %}
    <p>Log in to administrator account to post new trip inforamtions!</p>
    {% endif %}
    </div>
```

### Success criteria: Navigation bar

My 5th success criteria requires a navigation bar that is present in every page that the user goes to and guide the users through the pages. I identified this re-accuring pattern of the bar being present on all the pages, so I decided to create a base template (base.html) that can be used and extended on all the pages. (**pattern recognition**)

I also applied **abstraction** as a computatinoal thinking skill here because instead of duplicating the code for the navigation bar on every page, I created a separate template that can be reused and extended as needed. This approach promotes efficiency and maintainability, as any changes made to the base template will automatically propagate to all the pages. So there will be no need for specific changes within each html files if I need to change the structure such as adding one more page. This would also make things easier for the future developers if they would like to add more pages to the website.

Below is the base template in html:

```.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {% if title %}
    <title>{{ title }} </title>
    {% else %}
    <title>Welcome</title>
    {% endif %}
    <link rel="stylesheet" href = "/static/mystyle.css">
</head>

<div class="navigation_bar"> {# nav bar #}
    {# add a logo #}
    <img src = "/static/IkouLogo.png" alt = "logo" width = "90" height = "90">

    <a href = {{  url_for("logout")  }}>Logout </a>
    <a href = {{  url_for("login")  }}>Login/Register </a>
    <a href = {{  url_for("posts")  }}>Share Your Experience </a>
    <a href = {{  url_for("planned_trips")  }}>Planned Trips</a>
    <a href = {{  url_for("home")  }}>Home </a>
    
</div>
<body>

{% block content %} {% endblock %}

</body>

</html>
```


## Criteria D



## Criteria E

### User Evaluation
- client ( with reference to the interview)
  - client feedback reference to appendix
- other user

### Recommendation for future development

#### 1
identify + justify

#### 2



# Appendix

## Appendix 1: Client interview - Purpose and requirements
![client_interview_notes](https://user-images.githubusercontent.com/100017195/236198304-4cd2324d-17b8-46e5-abe6-c01ac45dd770.jpeg)
**Attatchment 1** Client interview notes

https://drive.google.com/file/d/1UpFwpFS8vu2FSt0gse6tdO1JlY3B_99_/view?usp=share_link

**Attatchment 2** Client interview recording (Gooogle Drive link)

## Appendix 2: Client interview - Feedback 


[^1]: “Back-End Development.” Benefits of Choosing Flask | Light IT. Accessed May 4, 2023. https://light-it.net/expertise/backend-development/flask/. 
