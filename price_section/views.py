from django.shortcuts import render
from django.views.generic import ListView
from .models import Crypto





class CryptoView(ListView):
    model = Crypto
    template_name = 'price_section/tracker.html'
    #def get_queryset(self):
        #cryptos = Crypto.objects.order_by('created_at')
        #return cryptos
