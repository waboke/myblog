
# Building A Blog Application With Django
<p>In this Course, we’ll build a Blog application with Django that allows users to create, edit, and delete posts. Click <a href="https://djangocentral.com/building-a-blog-application-with-django/" target="_blank">Here</a> to have a comprehensive review of what we shall be building in this course.</p>

## Installation Instructions
<p>If you want to work with this project or create a version of it make sure to follow the steps below!</p>

<p>Make sure to install Python 3, pip and virtualenv</p>

<ol> 
  <li> Create a project folder </li>

    $ mkdir project
    $ cd project
<li> Create a python 3 virtualenv, and activate the environment to install requirements.</li>

    $ python3 -m venv env
    $ source env/bin/activate
<li> Install the project dependencies from requirements.txt </li>

    (env)$ pip install -r requirements.txt
<li> Clone the repository</li>

    (env)$ git clone https://github.com/waboke/myblog.git
    (env)$ cd myblog
</ol
You have now successfully set up the project on your environment.

## How to run the project?
Make sure you are in env and then do the following each at a time.

(env)$ python manage.py makemigrations
(env)$ python manage.py makemigrations blogApp
(env)$ python manage.py makemigrations users
(env)$ python manage.py migrate
(env)$ python manage.py createsuperuser
(env)$ python manage.py runserver
## Features
### Blog list View
List all blog posts with Title, Tag, Number of total comments(working on for v1.2), Author Name, Date Posted, Image, and some body part with Read More button.

### Recent Posts
List all the post which are created recently with Image thumb and Title.

### category list
List all the categories related to the posts with total number of posts each categories have.

### Search
List all blog posts with the search query that you enter.

### Pagination
To limit with a certain number of posts in each page.

### Blog Detail View
To view the complete blog post when clicked on Read More or on the Title.

### Features for v1.2
Login/Register
Users can Login/Register to the Blog App.

### Comment
Users can comment to any blog post after login or comment anonymously without login.

### Create Blog Post
Users can create blog posts from the front end and add for approval, by the admin.

### Edit Profile
Users can edit Profile Image, First Name, Last Name, Email id, username, password.

### Tech Stacks
Language: Python 3.7
Framework: Django 3.1.5
Latest Fixes
Added Unique Slug Generator based on Title
Dynamic Title Tag for Blog Details
## How you can contribute to this project?
<ol>
<li>Fork this project to your GitHub account</li> 
<li>Clone the repository to your local machine and follow the above Installation instructions</ol>
<li>Find an issue or feature and work on it</li>
<li>Make a pull request</li>
</ol>



