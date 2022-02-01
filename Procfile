web: gunicorn movies_backend.wsgi
release: python manage.py makemigrations
release: python manage.py collectstatic
release: python manage.py migrate