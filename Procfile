release: python manage.py migrate
celery: celery -A PaginaCoinsmos worker --loglevel=INFO
web: gunicorn PaginaCoinsmos.wsgi
