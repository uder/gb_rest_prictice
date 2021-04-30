#!/bin/bash

while true; do
	if $(/bin/nc -z db 5432); then
		break
	fi
	echo "Wainting Db..."
	sleep 5
done

if [ ! -f /python/.env ]; then
	secret=$(/usr/local/bin/python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
	echo "SECRET_KEY='$secret'" > /python/.env
fi

cd /python

/usr/local/bin/python3 manage.py migrate
#/usr/local/bin/python3 /python/manage.py create_data
/usr/local/bin/python3 /python/manage.py runserver
#gunicorn todo.wsgi -b 0.0.0.0:8000
