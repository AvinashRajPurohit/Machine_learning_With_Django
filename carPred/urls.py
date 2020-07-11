from .views import prediction,home
from django.urls import path, include

urlpatterns = [
    path('', home, name='home'),
    path('predict/', prediction, name='predict'),
]
