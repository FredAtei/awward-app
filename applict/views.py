from django.shortcuts import render,redirect
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm,UpdateUserProfileForm
from django.http import HttpResponseRedirect, JsonResponse
from django.http  import HttpResponse,Http404

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
        'profile':profile  

    }
    return render(request, 'profile.html', params)    

def addprofile(request):
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            # return redirect('profile')
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)

    params = {   
        'user_form': user_form,
        'prof_form': prof_form,
        
    }
    return render(request, 'add_profile.html', params )    