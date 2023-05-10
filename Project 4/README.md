# Ikou Network
![image](https://user-images.githubusercontent.com/100017195/236658316-9ffe5290-ec10-480e-b00d-01e3d29351f4.png)

**Fig 1** Project Ikou Logo designed by Vera Hoffman

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

Design overview:

1. Problem define
2. Ouline solution
3. Planning
4. Development
5. Beta testing
6. Gather feedback
7. Implementation of feedback
8. Final beta testing
9. Final feedback on future development

#### diagrams
- System Diagram.
![system_diagram_U3_project](https://github.com/idrlykforeal/Unit-4/assets/100017195/752d458b-45c7-4a26-b110-93cd10858b13)
**Fig 2** System diagram of Ikou Network

- Flow diagrams for algorithms.
![flow_login](https://user-images.githubusercontent.com/100017195/236600976-197924e9-e8e8-45b4-b83a-5c777c814b3a.jpeg)

**Fig 3** Flow diagram for login algorithm

![API flowchart example](https://user-images.githubusercontent.com/100017195/236601032-379bff5e-531a-49d4-b1b9-0ba24570ad3a.jpeg)

**Fig 4** Flow diagram for validation of username

![flow_adminposts](https://user-images.githubusercontent.com/100017195/236601041-4a998e3a-5c19-4827-9822-0aa972b000d7.jpeg)

**Fig 5** Flow diagram for administrator post algorithm


- Database ER diagram 
<img width="957" alt="image" src="https://user-images.githubusercontent.com/100017195/236351392-7371d4fb-27a7-4472-942f-9990d4e19202.png">

**Fig 6** ER diagram for example data entities used

  - example data:
<img width="665" alt="image" src="https://user-images.githubusercontent.com/100017195/236601117-bec92def-ee34-468c-a848-0030c499f9a5.png">

**Fig 7** Screenshot example of how the user table is structured

<img width="1144" alt="image" src="https://user-images.githubusercontent.com/100017195/236601254-9f437f14-d618-47a6-9498-08868471ccd4.png">

**Fig 8** Screenshot example of how the posts table is structured

- UML diagram

![image](https://github.com/idrlykforeal/Unit-4/assets/100017195/c0aa2c84-1a31-490f-8f20-3973496086dc)

**Fig 9** UML diagram of the only class used(database worker)


- Annotated screen mockups or wireframes.
![wiafram](https://user-images.githubusercontent.com/100017195/236349210-16fc96d9-19c5-4a13-bfbd-4b38059ebc4f.jpg)
**Fig 10** Wireframe diagram for Ikou Network.

### Record of Tasks
| Task No |                              Planned Action                              |                                                                                          Planned Outcome                                                                                          | Time estimate | Target completion date | Criterion |
|:-------:|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------:|:----------------------:|:---------:|
|       1 | Planning: meet my client                                                 | address the problem that the client is facing.                                                                                                                                                    | 10 mins       |                  Apr 6 | A         |
|       2 | Planning: Write problem definition                                       | extending from the client problem, come up with a clear problem definition that the client is facing in detail.                                                                                   | 10 mins       |                  Apr 6 | A         |
|       3 | Planning: Write the proposed solution and rationale for propsed solution | My client is able to see what I am creating as a solution and input feedback so that he gets what he wants                                                                                        | 20 mins       |                 Apr 10 | A         |
|       4 | Planning: Write the design statement                                     | Able to proceed with a clear plan and goal now that the design statement is written                                                                                                               | 10 mins       |                 Apr 10 | A         |
|       5 | Planning: Client interview                                               | Interview the client, present them with my proposed solution and confirm their needs. Also ask if they are satisfired with the proposed solution, and what they would like to add apon it.        | 5 mins        |                 Apr 13 | A         |
|       6 | Planning: Write each success criteria                                    | Have a clear outline of what is needed to be acheived for my client so I am able to fulfill the clients needs                                                                                     | 25 mins       |                 Apr 14 | A         |
|       7 | Design: Create the system diagram                                        | Can showcase what the whole website will look like and what files and programs it will run                                                                                                        | 25 mins       |                 Apr 17 | B         |
|       8 | Design: Create the wireframe diagram                                     | We can showcase what the website program will look like, and i have a plan for how to style it using HTML and CSS                                                                                 | 25 mins       |                 Apr 18 | B         |
|       9 | Design: Create the flow diagram for key functions                        | Create flow diagrams that use natural language to showcase how the main function of the program would be structured and executed.                                                                 | 25 mins       |                 Apr 18 | B         |
|      10 | Develop: Build HTML template                                             | create base template HTML code that can be used for all pages with the top navigation bar.                                                                                                        | 25 mins       |                 Apr 20 | C         |
|      11 | Develop: Build HTML page displays                                        | create the general structure for all pages, no functionalities                                                                                                                                    | 25 mins       |                 Apr 21 | C         |
|      12 | Develop: Create the databases                                            | create the databases for users, posts, and admin posts                                                                                                                                            | 10 mins       |               April 22 | C         |
|      13 | Develop: Create validation functions                                     | code validation functions that validates email, username, password match and password length that could be used repeatedly in future program development                                          | 30 mins       |               April 25 | C         |
|      14 | Develop: User register                                                   | realize user register, data stored in database                                                                                                                                                    | 45 mins       |               April 30 | C         |
|      15 | Develop: User login                                                      | realize user login, create cookies when user successfully loged in, validation of username and password match                                                                                     | 45 mins       |               April 30 | C         |
|      16 | Develop: Posts                                                           | realize post function of storing the title and content into database                                                                                                                              | 45 mins       |                  May 1 | C         |
|      17 | Develop: Post pictures                                                   | refine post--upload pictures, where to store, how to access                                                                                                                                       | 60 mins       |                  May 1 | C         |
|      18 | Develop: Posts                                                           | validation of user input in posts, picture, and content cannot be empty                                                                                                                           | 30 mins       |                  May 1 | C         |
|      19 | Develop: Admin only posts                                                | realize the restricted display of administration restricted content                                                                                                                               | 45 mins       |                  May 1 | C         |
|      20 | Develop: Log out                                                         | realize log out function, clear all the cookies                                                                                                                                                   | 10 mins       |                  May 1 | C         |
|      21 | Test: create test plans                                                  | create detailed test plans for the prototype, test functions including login, register, post. All types of test including unit test, integrated test, and non-functional test                     | 20 mins       |                  May 4 | D         |
|      22 | Test: execute test plans                                                 | execute the test plans that have been done                                                                                                                                                        | 10 mins       |                  May 4 | D         |
|      23 | Test: beta testing                                                       | ask the client to test the prototype once, gather feedbacks on implementation                                                                                                                     | 20 mins       |                  May 5 |           |
|      24 | Implement: debug                                                         | implement all bugs that arose from the testings if applicable                                                                                                                                     | 30 mins       |                  May 5 | C, D      |
|      25 | Implement: beta testing                                                  | implement the suggestions from the client from the beta testing                                                                                                                                   | 50 mins       |                  May 6 |           |
|      26 | Evaluation: client and other user                                        | ask the client and another user to do beta testing on the program.                                                                                                                                | 45 mins       |                  May 6 | E         |
|      27 | Evaluation: client and user interview                                    | conduct interviews with the client and user that have used the prototype website. confirm if the success critera are met, and gather further feedback/recommendations that could be implemented.  | 10 mins       |                  May 6 | E         |
|      28 | Implement: implement recommendations                                     | implement the recommendations that were gathered in the interview with the user and the client after their beta testing                                                                           | 45 mins       |                  May 7 | C, E      |


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
9. OOP (object oriented programming)

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
Separating admin and regular users is one of the most key and interesting part of my project, I will explain it in detail:

This code presents a function `add_user` that adds a user to a database, setting their admin status based on their email address, and a list `admin_emails`:
`admin_emails` is a list that contains email addresses of admin users. It stores a predefined set of email addresses that are considered as admin emails.
`add_user(email, username, password)` is the start of the definition of the functino that populate tha user information to the database. It takes three parameters: `email`, `username`, and `password`.
I first connect to the database with `db = database_worker("ikou_network.db")` and then set variable`is_admin = False`. It will be used to determine if the user being added is an admin based on their email, and switched to True if the email is an admin email.
Next, I used a for loop `for i in admin_emails:` that iterates over the `admin_emails` list. Inside the loop, it checks if the `email` parameter matches any email address in the `admin_emails` list. If a match is found, the `is_admin` variable is set to `True`.
When the loop ends, I created a query string that includes `email`, `username`, `password`, and `is_admin` values, inserting these values into a table named `users` in the database. Finally, the query is executed and the repective data are stored. 


Continue with the break down of this aim, with **pattern recognition** I recognized the frequent usage of adding users and validation within the development of login and registration. So, in my library of code Mylib.py, I wrote functions that help add users (displayed above) and validations that can be called in the main app.py to avoid repetition and improve the efficiency of the code. Example of validating email and password shown below:

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

This code is interesting because although it is a HTML code, it also has python in it, I will explain: 

`{% if title %}` is a conditional statement that checks if the variable title exists and is not empty. Here it is used to check if a value has been passed to the template for the title variable. If the title variable exists and is not empty, title will appear, where the `title` is a variable from the python code, and is used in html in the following form `<title>{{ title }} </title>`.
On the other hand, if the title variable does not exist or is empty, the code will fall into the `{% else %}` block. In this case, a default title of "Welcome" is provided instead, using the line `<title>Welcome</title>`. The conditional statment ends with `{% end if %}`

Ahother interesting part is that everything outside the `{% block content %} {% endblock %}` can be repeated in all html templates that employ the template, and could insert more content within `{% block content %} {% endblock %}` as shown below.

```.py
{% extends "base_template.html" %}

{% block content %}

    # code not shown for simplicity

{% endblock %}
```


## Criteria D

video link:

https://youtu.be/tKwbiUv46QY

(refer to Appendix 4 for plan transcript of video structure)


## Criteria E

### User Evaluation

After showing the client the first prototype and gathering feedback for implementation (refer Appendix 2), I showed the final product to the client again, and some other users for evaluation with a last beta test. I conducted interviews (refer Appendix 3) with the client and other users, and gathered feedbacks for each success criteria, and general feedback for future development. The feedback is organized into 2 tables shown below. 

### Client
|                                                                                               Critieria                                                                                              | Met or not? |                                                     Feedback                                                    |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------:|:---------------------------------------------------------------------------------------------------------------:|
| the website has a login and registration system, where users will be separated into administrators and regular users, administrators can only be registered with the emails of the CAS group members | yes         | satisfired, especially the administrator account management, good                                               |
| the website allows all logged in users to create a post, including title, content, and upload pictures                                                                                               | yes         | good that it implemented the last feedback of displaying username and userid                                    |
| the website has a section for posting planned trips that is protected that is only accessable to administrators                                                                                      | yes         | good, no feedback                                                                                               |
| all viewers, no matter logged in or not, are able to view user posts and administrator posts which indludes post title, content, time, and picture                                                   | yes         | good, could improve by adding a like and commenting system                                                      |
| the website includes a top navigation bar that is visible on every page that guides users to each page.                                                                                              | yes         | good, no feedback                                                                                               |
| the website displays information about Project Ikou includes project goals, general introduction to the project, and pictures on the home page.                                                      | yes         | good, apart from a home page, could be good if there is also a new page of "my account" for all logged in users |

### Other users
|                                                                                               Critieria                                                                                              | Met or not? |                                                     Feedback                                                    |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------:|:---------------------------------------------------------------------------------------------------------------:|
| the website has a login and registration system, where users will be separated into administrators and regular users, administrators can only be registered with the emails of the CAS group members | yes         | satisfired, especially the administrator account management, good                                               |
| the website allows all logged in users to create a post, including title, content, and upload pictures                                                                                               | yes         | good that it implemented the last feedback of displaying username and userid                                    |
| the website has a section for posting planned trips that is protected that is only accessable to administrators                                                                                      | yes         | good, no feedback                                                                                               |
| all viewers, no matter logged in or not, are able to view user posts and administrator posts which indludes post title, content, time, and picture                                                   | yes         | good, could improve by adding a like and commenting system                                                      |
| the website includes a top navigation bar that is visible on every page that guides users to each page.                                                                                              | yes         | good, no feedback                                                                                               |
| the website displays information about Project Ikou includes project goals, general introduction to the project, and pictures on the home page.                                                      | yes         | good, apart from a home page, could be good if there is also a new page of "my account" for all logged in users |


### Recommendation for future development

According to the interviews with the client and other users(appendix 3), below are the suggestions for future development. 

#### Like and comment system

Both users and client suggest that in the post section, it would be great if other users can like the posts and make comments below. 
A like and comment system could be implemented since it would increase the user engagement since it can enhance the user experience by letting users have the ability to interact with the content that other users posted and express their opinions on the posts. This would encourage active participation and would promote a sense of community for the social platform. Comments also allow all the users contribute their knowledge and enrich the given content of the website, it is a utilization of audience. 

#### My account page

Another suggestion for future development would be a "My account" page, where it includes all posts that the logged in user has posted. This would be helpful for users as it provides a concentrated page for them to view their journey on this platform. User log-out could also be moved to this page to put all user-oriented content together for the user. 

#### Sort posts by location

Other users suggested that posts could be sorted according to the location that the trips take place or where the tourist attraction is located. There can also be a sub page guide to each location. 
This would have a enhanced user navigation since sorting posts by location allows users to easily find and explore content that is relevant to their desired destinations. It also helps by provide users with the geographic context users can access comprehensive information about a particular destination or tourist attraction, which would enhance their understanding and planning of trips.

# Appendix

## Appendix 1: Client interview - Purpose and requirements
![client_interview_notes](https://user-images.githubusercontent.com/100017195/236198304-4cd2324d-17b8-46e5-abe6-c01ac45dd770.jpeg)
**Attatchment 1** Client interview notes

https://drive.google.com/file/d/1UpFwpFS8vu2FSt0gse6tdO1JlY3B_99_/view?usp=share_link

**Attatchment 2** Client interview recording (Gooogle Drive link)

## Appendix 2: Client beta test feedback
![client_beta_feedback](https://user-images.githubusercontent.com/100017195/236658824-678339ad-9917-4ea4-97f3-69e85185974a.jpeg)
**Attatchment 3** Notes from client feedback from the first beta testing of the prototype.

## Appendix 3: Evaluation interview notes
![Final_evaluation_feedback](https://user-images.githubusercontent.com/100017195/236658978-9d379dd8-1c11-448d-ab38-57b69263b0b5.jpeg)
**Attatchment 4** Notes from client and other user after final beta testing of evaluation, recomendation suggestions for future development.

## Appendix 4: Video planning
![video_written_script_outline](https://user-images.githubusercontent.com/100017195/236661728-496c21db-6aa0-4911-b075-e791ae4b7fac.jpeg)
**Attatchment 5** Video planning document: written script outline

[^1]: “Back-End Development.” Benefits of Choosing Flask | Light IT. Accessed May 4, 2023. https://light-it.net/expertise/backend-development/flask/. 
