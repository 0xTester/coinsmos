release: python manage.py migrate
web: gunicorn PaginaCoinsmos.wsgi
celery: celery -A worker  PaginaCoinsmos -l info -c 4
