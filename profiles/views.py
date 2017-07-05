
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .forms import  ProfileForm
from .models import Profile
from django.views.generic import ListView


User = get_user_model()

@login_required
def profile_user(request):
	user = get_object_or_404(User, username=request.user)
	#name = get_object_or_404(name, username=request.name)
	profile, created = Profile.objects.get_or_create(user=user)
	
	context = {
		"profile": profile,
				}
	return render(request, "profiles/profile_user.html", context)


@login_required
def profile_edit(request):
	title = "Update Profile"
	profile, created = Profile.objects.get_or_create(user=request.user)
	form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect("profile_user")
	context = {
		"form": form,
		"title": title,
				}
	return render(request, "forms.html", context)



@login_required
def profile_view(request, username):
	user = get_object_or_404(User, username=username)
	profile, created = Profile.objects.get_or_create(user=user)
	 
	context = {
		"profile": profile,
		
				}
	return render(request, "profiles/profile_view.html", context)
	
 
	
class ProfileListView(ListView):
    
    def get_queryset(self, *args, **kwargs):
        qs = Profile.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                    Q(content__icontains=query) |
                    Q(user__username__icontains=query)
                    )
        return qs