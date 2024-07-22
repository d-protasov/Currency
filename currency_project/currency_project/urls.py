from django.urls import path
from currency.views import get_current_usd

urlpatterns = [
    path('get-current-usd/', get_current_usd),
]
