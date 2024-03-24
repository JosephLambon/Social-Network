# Social Networking Site
>### A CS50W project

## Contents
1. [Project Synopsis](#project_synopsis)
2. [Project Resources](#project_resources)
3. [Setup and Usage](#setup)
4. [Video Demo](#video)


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
#### [NOTE: Any lines of code included are intended for the command line]

### 1. Install prerequisites
a. Install [Python](https://www.python.org/) </br>
b. Install [virtualenv](https://virtualenv.pypa.io/en/latest/)
``` 
 pip install virtualenv
```
### 2. Setup virtual environment
* Create virtual environment </br>
```
# Run this line on the command line
# Replace 'env_name' with whatever your desired env's name is.

virtualenv env_name
```
* Start virtual environment
```
# This will activate your virtualenv.

source env_name/bin/activate
```
* Install django
```
# Running this in your command line will install it to you activated virtual environment

pip install django
```
### 3. Change directory
* Change into the 'project4' folder.
### 4. Make migrations in Django
```
# Check for any alterations to your project that need migrating

python manage.py makemigrations
```
```
# Make/push any migrations.

python manage.py migrate
```
### 5. Run django server
```
# This will host the web application locally

python manage.py runserver
```

## <a id='video'> Video Demo </a>

For this project, we were required to make a video displaying our web application's functionality. Feel free to watch this short exmaple of the final product. There are timestamps in the bio showing each of the implemented features.

<a href= 'https://youtu.be/dvlD1rxNW_I'>
<img width="1494" alt="Thumbnail" 
 src="https://github.com/JosephLambon/project4/assets/107887718/95ce679e-a5f9-4110-8615-8856dc3f7f30">
</a>



