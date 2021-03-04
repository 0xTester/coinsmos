release: python manage.py migrate
web: gunicorn PaginaCoinsmos.wsgi
celery: celery -A PaginaCoinsmos worker --loglevel=INFO
