from django.shortcuts import render
from .models import Picture
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    pictures = Picture.objects.all()
    ctx = {'pictures': pictures}
    return render(request, 'awards/index.html', ctx)