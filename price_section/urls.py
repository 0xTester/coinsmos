from django.urls import path
from . import views
from .views import CryptoView

urlpatterns = [
    path('', CryptoView.as_view(), name='price-home'),


]
# celery: celery -A PaginaCoinsmos worker --loglevel=INFO
