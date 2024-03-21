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
### 1. Install prerequisites
* Install [Python](https://www.python.org/)
* Install [virtualenv]
  > Use 'pip install virtualenv'
### 2. Setup virtual environment
* Start virtual environment
...virtualenv venv/bin/activate
* Install django
> * pip install django
### 3. Change directory
* Change into the 'project4' folder.
### 4. Make migrations in Django
> 1. python manage.py makemigrations
> 2. python manage.py migrate
### 5. Run django server
* python manage.py runserver
