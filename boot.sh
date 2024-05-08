#!/usr/bin/env sh
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn --bind :80 --workers 3 cashit.wsgi
#python manage.py runserver 0.0.0.0:80
