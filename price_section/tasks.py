from time import sleep
from celery import shared_task
from celery import Celery
from .models import Crypto
import urllib3
import json
import re

@shared_task
def crawl_currency():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=20&page=1&sparkline=false&price_change_percentage='24h'"

    #response = requests.get(url,verify=certifi.where())
    #transaction_content = response.json()

    http = urllib3.PoolManager()
    response = http.request('GET', url)
    #response = requests.get(url,verify=certifi.where())
    transaction_content=json.loads(response.data.decode('utf-8'))

    for crypto_content in transaction_content:
        Crypto.objects.create(
        cryptocurrency = crypto_content["name"],
        precio = crypto_content["current_price"],
        marketcap = crypto_content["market_cap"],
        volumen = crypto_content["total_volume"],
        supply = crypto_content["circulating_supply"],
        change = crypto_content["price_change_percentage_24h"],
        imagen = crypto_content["image"]
        )

        sleep(3)

@shared_task
def update_currency():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=20&page=1&sparkline=false&price_change_percentage='24h'"
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    transaction_content=json.loads(response.data.decode('utf-8'))
    pattern = re.compile(r'.*(?=\.)')
    pattern2 = re.compile(r'(.*)\.\d\d')
    id1 = 76
    for crypto_content in transaction_content:
        supply = crypto_content["circulating_supply"]
        change = crypto_content["price_change_percentage_24h"]
        match = pattern.match(str(supply))
        match2 = pattern2.match(str(change))
        data = {'cryptocurrency': crypto_content["name"], 'precio': crypto_content["current_price"],
                'marketcap': crypto_content["market_cap"], 'volumen': crypto_content["total_volume"],
                'supply': match[0], 'change': match2[0], 'imagen': crypto_content["image"] }

        Crypto.objects.filter(id=id1).update(**data)

        id1 += 1


if not Crypto.objects.all():
    crawl_currency()

while True:
    sleep(15)
    update_currency()
