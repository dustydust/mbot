#!/bin/bash

python ./backend/manage.py makemigrations
python ./backend/manage.py migrate
python ./backend/manage.py collectstatic --no-input
python ./backend/manage.py fixture_loaddata_all

exec "$@"