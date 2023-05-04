# Ikou Network

## Criteria A

### Problem Definition
The problem addressed by the "Project Ikou" CAS group is a lack of a centralized platform for the group to manage project informations. The group wants a platform where everyone can view project introduction, project information, and the future trips that are planned for the project. The group wants viewers to be able to create their own account and share their own travelling experience with photos and blog post content, which all viewers of the website can read. The group also wants to have administrator accounts, where they are the only ones able to update future trip plans with posts. The group also want the website to have a clear organization that displays and guides viewers to each page. 

### Proposed Solution
As part of the CAS group, I discussed with my group mates, and confirmed that the client(Project Ikou) would like to have a website with Python Flask using the languages of python, HTML, and CSS. The website should have a log in and sign up system, that also assigns the project members as administrators, where user informations are stored in SQLite database. The website allows users to post and administrators to post extra contents, where the title, content, and photos uploaded by the users are stored in another table in the SQLite database. The website fetches data from the database to display the user and administrator posts.


### Rationale for Proposed solution
A website would be the perfect platform because it is one of the most accessible platforms that can run on browsers which all users will be able to have. It also allows all the requirements of Project IKOU: it has post and get requests that allow users to register and login, and create posts.

Python Flask is a great tool to develop websites because it is simple and flexible. Flask provides a lightweight and modular structure that allows developers to build web applications quickly and easily. With a built-in development server and support for multiple extensions, Python Flask can be used to add functionality to the application. Flask is particularly suitable for small to medium-sized web applications with low to medium traffic, which is what we are aiming for. 

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

## Criteria C
