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
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from game.views import GameViewSet
from game.views import PublisherGamesRateViewSet
from game.views import UsersAvgAgeViewSet
from user.views import UserViewSet
from user.views import UserInfoViewSet
from publisher.views import PublisherAPIView
import genre.views


router = SimpleRouter()

router.register(r'games', GameViewSet, basename='game')
router.register(r'users', UserViewSet, basename='user')
router.register(r'user_info', UserInfoViewSet, basename='user-info')
router.register(r'games_rate', PublisherGamesRateViewSet, basename='user-info')
router.register(r'users_age', UsersAvgAgeViewSet, basename='users-age')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', genre.views.genres_list),
    path('genres/<int:pk>/', genre.views.genres_details),
    path('publishers/', PublisherAPIView.as_view(), name='publisher-list'),
    path('publishers/<int:pk>/', PublisherAPIView.as_view(), name='publisher-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns += router.urls

