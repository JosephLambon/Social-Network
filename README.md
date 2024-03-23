# Social Networking Site
>### A CS50W project

## Contents
1. [Project Synopsis](#project_synopsis)
2. [Project Resources](#project_resources)
3. [Setup and Usage](#setup)
4. [Video Example](#video)


## <a id='project_synopsis'> Project Synopsis </a>
The aim of this project was to design a Twitter-like social network website. 

Using Django for the backend and React for the frontend, I developed a functional web application in which you can make posts, follow other users, like posts and edit your own.

## <a id='project_resources'> Project Resources </a>
* [Django](https://www.djangoproject.com/)
> Django is a high-level open source Python framework that makes it easier to build secure web applications.

* [React](https://react.dev/)
> React is a JavaScript framework that enables you to build slick user interfaces and build custom re-usable components.

* [Bootstrap](https://getbootstrap.com/)
> Bootstrap is a front-end library, offering pre-built components and JavaScript plug-ins.

* [SQLite](https://www.sqlite.org/)
> SQLite is a C-language library that implements a fast & reliable SQL database engine.

## <a id='setup'> Setup and Usage </a>
#### [NOTE: Anything in quotations ('...') is for the command line]

### 1. Install prerequisites
a. Install [Python](https://www.python.org/) </br>
b. Install [virtualenv](https://virtualenv.pypa.io/en/latest/)
  > 'pip install virtualenv' 
### 2. Setup virtual environment
* Create virtual environment </br>
   > 'virtualenv env_name' </br>
* Start virtual environment
   > 'source env_name/bin/activate' </br>
* Install django
   > 'pip install django'
### 3. Change directory
* Change into the 'project4' folder.
### 4. Make migrations in Django
> 'python manage.py makemigrations' </br>
>'python manage.py migrate'
### 5. Run django server
> 'python manage.py runserver'

## <a id='video'> Video Example </a>

For this project, we were required to make a video displaying our web application's functionality. Feel free to watch this short exmaple of the final product. There are timestamps in the bio showing each of the implemented features.
[![IMAGE ALT TEXT HERE](https://i9.ytimg.com/vi/NsjxrR-SHyg/mqdefault.jpg?sqp=CODJ-K8G-oaymwEmCMACELQB8quKqQMa8AEB-AH-CIAC0AWKAgwIABABGGsgayhrMA8=&rs=AOn4CLDSH_FJGtgX5TLtIK7kWgfN77oZQg)](https://youtu.be/NsjxrR-SHyg)
