from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('inicio', views.inicio, name='index'),
    path('creditos', views.creditos, name='credits'),
    path('creditos/new', views.newCredito, name='newCredit'),
    path('creditos/pay', views.payCredito, name='payCredit'),
]