"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from blog_auth.views import signup_view, login_view, logout_view
from account.views import account_view
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('account/<str:username>', account_view, name='account'),
    path('accont/logout/', logout_view, name="logout"),
]

