release: python manage.py migrate
web: gunicorn PaginaCoinsmos.wsgi
celery: celery worker -A PaginaCoinsmos -l info -c 4
