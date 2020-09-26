from django.urls import path

from . import views

app_name = 'reg'
urlpatterns = [
    path('', views.registratsioon, name='reg'),
]
