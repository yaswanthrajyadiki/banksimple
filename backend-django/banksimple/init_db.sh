#!/usr/bin/env bash

echo "------ Create database tables ------"
python manage.py migrate --noinput

echo "------ create default admin user ------"
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@banksimple.local', 'Passw0rd')" | python manage.py shell

echo "------ starting gunicorn &nbsp;------"
gunicorn banksimple.wsgi --workers 2