release: python manage.py migrate
web: gunicorn PaginaCoinsmos.wsgi
worker: celery -A PaginaCoinsmos worker --loglevel=INFO
