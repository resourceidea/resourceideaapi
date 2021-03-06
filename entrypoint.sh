#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    echo "$POSTGRES_HOST"
    echo "$POSTGRES_PORT"

    while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
        sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py setupsuperuser

exec "$@"