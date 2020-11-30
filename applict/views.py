from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile, Project,Rating
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm,UpdateUserProfileForm,ProjectForm
from django.http import HttpResponseRedirect, JsonResponse
from django.http  import HttpResponse,Http404
from django.db.models import Avg
from rest_framework import status

# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    posts = Project.objects.all()
    users = User.objects.exclude(id=request.user.id)
    current_user = request.user

    return render(request, 'awards/index.html',{'posts':posts,'user':current_user,'users':users})

@login_required(login_url='/accounts/login')
def profile(request,profile_id):
    profile = Profile.objects.filter(id=profile_id)
    # images = request.user.profile.images.all()
    current_user = request.user
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST )
        profile_form = UpdateUserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            profile_form.save()
            bio = user.bio
    else:
        user_form = UpdateUserForm()
        prof_form = UpdateUserProfileForm()
    params = {
        'user_form': user_form,
        'profile_form': prof_form, 
        'profile':profile  

    }
    return render(request, 'profile.html', params)    

def addprofile(request):
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            profile_form.save()
            # return redirect('profile')
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateUserProfileForm(instance=request.user.profile)

    params = {   
        'user_form': user_form,
        'profile_form': prof_form,
        
    }
    return render(request, 'add_profile.html', params )  

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('Home')
    else:
        form = ProjectForm()
    return render(request, 'newpost.html', {"form": form})   

def projects(request, c_id):
    current_user = request.user
    current_project = Project.objects.get(id=c_id)
    ratings = Rating.objects.filter(post_id=c_id)
    usability = Rating.objects.filter(post_id=c_id).aggregate(Avg('usability'))
    content = Rating.objects.filter(post_id=c_id).aggregate(Avg('content'))
    design = Rating.objects.filter(post_id=c_id).aggregate(Avg('design'))

    return render(request, 'viewproject.html',{"project": current_project, "user": current_user, 'ratings': ratings, "design": design,"content": content, "usability": usability})      