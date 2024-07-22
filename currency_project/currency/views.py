from django.shortcuts import render
from django.http import JsonResponse
import requests
import time

last_requests = []


def get_current_usd(request):
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    data = response.json()

      # Добавляем текущий запрос в список последних запросов
    last_requests.append(data['rates']['RUB'])
    if len(last_requests) > 10:
            last_requests.pop(0)

        # Пауза перед возвратом данных
    time.sleep(10)

    
    return JsonResponse({
            'current_usd_to_rub': data['rates']['RUB'],
            'last_10_requests': last_requests
        })
