from api.views import ShortenerCreateApiView, ShortenerListAPIView, ShortenerInfo
from django.urls import path, include
from api import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


app_name='api'
router = routers.DefaultRouter()
router.register('groups', views.GroupViewSet)
router.register('users/register', views.CreateUserView)


urlpatterns = [
    path('',ShortenerListAPIView.as_view(),name='all_links'),
    path('create/',ShortenerCreateApiView.as_view(),name='create_api'),
    path('info/<int:pk>',ShortenerInfo.as_view(),name='info'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('get-token/', obtain_auth_token, name='api_token_auth'),
]