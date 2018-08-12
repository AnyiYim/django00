from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from backend import views

urlpatterns = [
    # path('test', views.api_text)

    # # 1.0
    # path('persons/', views.person_list),
    # path('persons/<int:pk>/', views.person_detail),

    # 2.0, 3.0, 4.0
    path('persons/', views.PersonList.as_view()),
    path('persons/<int:pk>/', views.PersonDetail.as_view()),
]

# 引进额外的url模式
urlpatterns = format_suffix_patterns(urlpatterns)
