#!/bin/sh
echo "Waiting for database..."
while ! pg_isready -h $DB_HOST -p 5432 -U $DB_USER; do
  sleep 1
done

python manage.py migrate
python manage.py runserver 0.0.0.0:8000