from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import View 
from audiotracks.models import get_track_model
from profiles.models import Profile 
from posts1.models import Post 

User = get_user_model()
tracks = get_track_model

class HomeView(View):

  def get(self, request, *args, **kwargs):
	
    posts = Post.objects.all().order_by("-timestamp")[:5]
    profiles = Profile.objects.all().order_by("-timestamp")[:1]
    tracks = get_track_model().objects
    tracks = tracks.order_by('-created_at').all()
    return render(request, "home.html", {
        "profile": Profile, 'tracks': tracks, 'post': Post,
    })

   
 
class SearchView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get("q")
        qs = None
        if query:
            qs = Profile.objects.filter(
                    Q(name__icontains=query)
                )
        context = {"profiles": qs}
        return render(request, "search.html", context)
		

          
      
	
       
		
		





    # def post(self, request, *args, **kwargs): # POST -- create view
    #     return HttpResponse("Hello")

    # def put(self, request, *args, **kwargs): # PUT -- update view
    #     return HttpResponse("Hello")

    # def delete(self, request, *args, **kwargs): # DELETE -- delete view
    #     return HttpResponse("Hello")		
		