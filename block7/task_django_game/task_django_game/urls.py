"""task_django_game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from rest_framework.generics import ListCreateAPIView
from rest_framework.routers import SimpleRouter

from game.views import GameViewSet
from user.views import UserViewSet
from publisher.views import PublisherAPIView
import genre.views

router = SimpleRouter()
router.register(r'games', GameViewSet, basename='game')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', genre.views.genres_list),
    path('genres/<int:pk>/', genre.views.genres_details),
    path('publishers/', PublisherAPIView.as_view(), name='publisher-list'),
    path('publishers/<int:pk>/', PublisherAPIView.as_view(), name='publisher-detail')
]

urlpatterns += router.urls

