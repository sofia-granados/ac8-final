#!/bin/sh
source .venv/bin/activate
python backend/manage.py runserver $PORT
