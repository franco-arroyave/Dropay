from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('statistics', views.statistics, name='statistics'),
]

urlpatterns += staticfiles_urlpatterns()