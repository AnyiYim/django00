"""text_vue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path, include
from django.views.generic import TemplateView
from oscar.app import application
from rest_framework import serializers, viewsets
from rest_framework.routers import DefaultRouter


# Serializers define the API representation.
# restful 的 序列化类
from backend.models import Person


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'age')


# 设置 view 的行为.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


# restful route
routers = DefaultRouter()
routers.register(r'user', UserViewSet)
routers.register(r'person', PersonViewSet)


urlpatterns = [
    path('i18n', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', include(routers.urls)),
    path('api_auth/', include('rest_framework.urls')),
    # path('', TemplateView.as_view(template_name='index.html')),
    path('api/', include(('backend.urls', 'api'), namespace='api'))
]
