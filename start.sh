#!/bin/bash

echo "Aplicando migrações..."
python manage.py migrate

echo "Iniciando Gunicorn..."
gunicorn biblioteca_pai.wsgi:application
