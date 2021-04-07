"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from todo.views import UserModelViewSet,ProjectModelViewSet,ToDoModelViewSet,UserGenericViewSet,DjangoUserGenericViewSet
from todo.views import schema_view
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.schemas import get_schema_view

router=DefaultRouter()
# router.register('user',UserModelViewSet)
router.register('user',UserGenericViewSet)
# router.register('djangouser',DjangoUserGenericViewSet)
router.register('project',ProjectModelViewSet)
router.register('todo',ToDoModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-jwt-auth/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api-jwt-auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^api/v(?P<version>\d)/djangouser/$',DjangoUserGenericViewSet.as_view({'get':'list'})),
    re_path(r'^api/v(?P<version>\d)/user/$',UserGenericViewSet.as_view({'get':'list'})),
    path('redoc/',schema_view.with_ui('redoc',cache_timeout=0),name='schema-redoc'),
    path('redoc-part/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='redoc-part'),
    path('openapi', get_schema_view(
        title='openapi',
        description='api',
        version='1'
    ),name='openapi-schema'),
]

