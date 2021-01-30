#!/bin/bash
python manage.py makemigrations
python manage.py migrate
gunicorn GhughuServer.wsgi --bind 0.0.0.0:8000 --workers 3
