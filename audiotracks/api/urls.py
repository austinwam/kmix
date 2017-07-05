from django.conf.urls import url
from django.contrib import admin

from .views import (
    TrackCreateAPIView,
    TrackDeleteAPIView,
    TrackDetailAPIView,
    #TrackListAPIView,

    )

urlpatterns = [
    #url(r'^$', TrackListAPIView.as_view(), name='list'),
    url(r'^create/$', TrackCreateAPIView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', TrackDetailAPIView.as_view(), name='detail'),
    #url(r'^(?P<slug>[\w-]+)/edit/$', ProfileUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', TrackDeleteAPIView.as_view(), name='delete'),
]
