# Iowa State - Lab Information Management System

## Purpose
This system is made for tracking plant lab samples, such as a seed inventory, and corresponding plants.

## Setup
The system is built with [django] 3.x, and python3 

### Pre-reqs:
* python3

### Setup a development environment
* clone this repo with `git clone --recursive`
* open a shell, and cd into this directory
* remove mysqlclient from requirements.txt
* Remove settings using environment variables from settings.py (currently Auth/File Uploads/Logging), change SECRET_KEY, change database to SQLite, set DEBUG to true
* install virtualenv: `pip3 install virtualenv`
* `virtualenv env -p $(which python3)`
* `source env/bin/activate`
* `pip install -r requirements.txt`
* `python manage.py migrate`
* `python manage.py createsuperuser`

[django]: https://www.djangoproject.com/

