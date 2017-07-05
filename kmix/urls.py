"""kemiz URL Configuration

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
from django.views.generic import TemplateView, RedirectView
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from .views import HomeView, SearchView
from django.conf.urls import url, include
from accounts.views import UserRegisterView
from profiles.app.views import ProfileSearchAPIView
from audiotracks.api.views import SearchAPIView
 
from django.conf import settings

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^profiles/', include('profiles.urls')),
	url(r'^posts/', include("posts1.urls", namespace='posts')),
	url(r'^api/posts/', include("posts1.api.urls", namespace='posts-api')),
	url(r'^api/profiles/', include("profiles.app.urls", namespace='profiles-api')),
	url(r'^api/audiotracks/', include("audiotracks.api.urls", namespace='audiotracks-api')),
    url(r'^admin/', admin.site.urls),
	url(r'^api/search/$', SearchAPIView.as_view(), name='search-api'), 
	url("^music/", include("audiotracks.urls")),
	url("^(?P<username>[\w\._-]+)/music/", include("audiotracks.urls")),
	 
    url(r'^search/$', SearchView.as_view(), name='search'),
	url(r'^', include('django.contrib.auth.urls')),
	url(r'^register/$', UserRegisterView.as_view(), name='register'),
	url(r'^app/search/$', ProfileSearchAPIView.as_view(), name='search-api'), 
 
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

