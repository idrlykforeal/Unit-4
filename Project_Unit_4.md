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

### I. Record of Tasks
template (0 without)
Includes all 5 stages of the design cycle (plan, design, develop, test, implement)
Planned action is specific and defined which results in the expected outcome (logical connection)
Relates to the product proposed in Criterion A (not a record of making some alternative product)
Should mainly cover the tasks involved in the development of the product
Updated during the life of the project (think about a daily entries)
Provides a realistic plan and timeline for managing the solution, including the gathering of necessary information, the development of the product, the testing process, and the implementation of the product.

### II. Design Overview

#### general outline of the product that is proposed in Criterion A
#### diagrams
- System Diagram.
- Flow diagrams for algorithms.--- in natural language!!!
- UML Diagram and Class Relationships (if an OOP methodology has been used).
- Database ER diagram (if a relational database has been used) with examples of how the data look like with normalization.
- Data dictionaries (for any data storage system uses).
- Annotated screen mockups or wireframes.


#### III. Test Plan


## Criteria C


# Appendix

## Appendix 1: Client interview - Purpose and requirements
![client_interview_notes](https://user-images.githubusercontent.com/100017195/236198304-4cd2324d-17b8-46e5-abe6-c01ac45dd770.jpeg)
**Attatchment 1** Client interview notes

https://drive.google.com/file/d/1UpFwpFS8vu2FSt0gse6tdO1JlY3B_99_/view?usp=share_link

**Attatchment 2** Client interview recording (Gooogle Drive link)

## Appendix 2: Client interview - Feedback 


[^1]: “Back-End Development.” Benefits of Choosing Flask | Light IT. Accessed May 4, 2023. https://light-it.net/expertise/backend-development/flask/. 
