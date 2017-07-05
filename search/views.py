from django.shortcuts import render
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from django.views.generic import View
from profiles.models import Profile
from audiotracks.models import get_track_model
tracks = get_track_model

class SearchView(View):
    pass


def tracks_list(request):
    queryset_list = tracks.objects.active().order_by("-timestamp")
    queryset_list = tracks.objects.all()
    
	
	
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
		       # Q(name__icontains=query)|
                Q(title__icontains=query)|
                Q(artist__icontains=query)
                ).distinct()
    paginator = Paginator(queryset_list, 12) # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset, 
        "title": "List",
        "page_request_var": page_request_var,
    }
    return render(request, "search.html", context)

