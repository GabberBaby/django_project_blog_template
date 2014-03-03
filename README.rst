Django project template
========================================

About
-----

This project template creates a Django 1.5 project with a base set of applications + zinnia + photologue + filebrowser

Prerequisites
-------------

- Python >= 2.6
- pip
- virtualenv (virtualenvwrapper is recommended)

Usage
-----
Create a Django project::

    mkdir my-website.com
    cd my-website.com
    django-admin.py startproject mywebsite . -e py,rst,example,gitignore --template=https://github.com/GabberBaby/django_project_template/archive/empty_project.zip

Installation
------------

To setup a local development environment::

    mkvirtualenv {{ project_name }}
    pip install -r requirements.txt
    ./manage.py syncdb --migrate
    ./manage.py runserver

