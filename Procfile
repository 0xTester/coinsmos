release: python manage.py migrate
web: gunicorn PaginaCoinsmos.wsgi
worker: celery worker --app=tasks.app
