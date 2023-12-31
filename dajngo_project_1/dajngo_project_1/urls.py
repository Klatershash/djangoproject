"""
URL configuration for dajngo_project_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from mySite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  views.index),
    path('contacts/',  views.contacts),
    path('blog/', views.blog),
    path('reg/', views.reg),
    path('auth/', views.auth),
    path('article/<int:id>', views.article_id),
    path('panel/', views.panel),
    path('logout/', views.logout),
    path('addarticle/', views.addarticle),
    path('users/', views.users),
    path('user/<str:login>', views.user_detail),
    path('add_avatar/', views.add_avatar),
    path('chat/<str:login>/', views.chat)
]



