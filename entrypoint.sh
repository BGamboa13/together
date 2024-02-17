#!/bin/sh

python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Start Gunicorn processes
gunicorn Together.wsgi:application --bind 0.0.0.0:8000