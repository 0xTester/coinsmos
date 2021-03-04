from django.shortcuts import render
from django.views.generic import ListView
from .models import Crypto





class CryptoView(ListView):
    model = Crypto
    template_name = 'price_section/tracker.html'
