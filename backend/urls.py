from django.conf.urls import url
from django.urls import path

from backend import views

urlpatterns = [
    # path('test', views.api_text)
    path('persons/', views.person_list),
    path('persons/<int:pk>/', views.person_detail),
]