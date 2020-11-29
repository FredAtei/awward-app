from django.shortcuts import render
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'awards/index.html')

@login_required(login_url='/accounts/login')
def profile(request,profile_id):
    profile = Profile.objects.filter(id=profile_id)
    # images = request.user.profile.images.all()
    current_user = request.user
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST )
        prof_form = UpdateUserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            bio = user.bio
    else:
        user_form = UpdateUserForm()
        prof_form = UpdateUserProfileForm()
    params = {
        'user_form': user_form,
        'prof_form': prof_form,
        # 'images': images, 
        'profile':profile  

    }
    return render(request, 'profile.html', params)    