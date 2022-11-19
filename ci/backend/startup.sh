#!/bin/bash

# Create databse and insert user
/opt/gate/venv/bin/python opener/create_user.py

# Remove envs
unset USERNAME PASSWORD

# Start the gunicorn process
/opt/gate/venv/bin/gunicorn opener.main:app -c gunicorn_conf.py
