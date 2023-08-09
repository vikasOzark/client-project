#!/bin/sh
echo "running"
python manage.py makemigrations --no-input
echo "migration complete"
python manage.py migrate --no-input
echo "migrate complete"
python manage.py collectstatic --no-input
echo "collect static complete"
gunicorn backend.wsgi:application --bind 0.0.0.0:8000 --reload --timeout 900
echo "bind gunicorn"