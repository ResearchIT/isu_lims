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
* Create a file set_env.sh with contents like the following
  ```
    export LIMS_SECRET_KEY='asdfasdfasdfasdfasdfasdfaasdfasdf'
    export LIMS_DEVEL_ACTIVE='IM_REALLY_SURE_THIS_ISNT_PRODUCTION'
    export LIMS_DEVEL_ADMIN_USERNAME='adminuser'
    export LIMS_DEVEL_ADMIN_PASSWORD='adminpassword'
    export LIMS_DEVEL_ADMIN_EMAIL='youremail@example.com'
   ```

* install virtualenv: `pip3 install virtualenv`
* `virtualenv env -p $(which python3)`
* `source env/bin/activate`
* `source set_env.sh`
* `pip install -r requirements.txt`
* `./reset.sh`

[django]: https://www.djangoproject.com/

