"""n2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from profiles import views 
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from .views import ProfileListView





urlpatterns = [
    url(r'^profile/edit/', views.profile_edit, name='profile_edit'),
    url(r"^profile/(?P<username>[\w.@+-]+)/$", views.profile_view, name='profile'),
    #url(r'^profile/Documents/add/$', views.Document_add, name='D_add'),
    #url(r'^profile/Documents/edit/$', 'profiles.views.Documents_edit', name='Documents_edit'),
    url(r'^search/$', ProfileListView.as_view(), name='list'), # /tw
    url(r"^profile/$", views.profile_user, name="profile_user"),
   
]
