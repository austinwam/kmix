from django.conf.urls import url
from django.contrib import admin

from .views import (
    ProfileCreateAPIView,
    ProfileDeleteAPIView,
    #ProfileDetailAPIView,
   #ProfileListAPIView,
   #ProfileUpdateAPIView,
    )

urlpatterns = [
    #url(r'^$', ProfileListAPIView.as_view(), name='list'),
    url(r'^create/$', ProfileCreateAPIView.as_view(), name='create'),
    #url(r'^(?P<slug>[\w-]+)/$', ProfileDetailAPIView.as_view(), name='detail'),
    #url(r'^(?P<slug>[\w-]+)/edit/$', ProfileUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', ProfileDeleteAPIView.as_view(), name='delete'),
]
