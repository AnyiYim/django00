from django.conf.urls import url
from django.urls import path

from backend import views

urlpatterns = [
    path('test', views.api_text)
]