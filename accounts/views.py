import os
import uuid
from pytube import YouTube
import uuid
import requests
from mutagen.mp3 import MP3
import datetime
import subprocess
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.files import File
from .forms import *
from moviepy.editor import VideoFileClip
from datetime import timedelta
from django.core.files.temp import NamedTemporaryFile
from .models import *
from .decorators import *
# Create your views here.
from django.http import FileResponse, JsonResponse
from django.shortcuts import redirect, get_object_or_404
#from .decorators import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, 'accounts/home.html')

@login_required(login_url='login')
def upload_video(request):
    form = VideoUploadForm()
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        
    context = {'form':form}
    return render(request, 'accounts/upload.html', context)

@unauthenticated_user
def register_page(request):
    
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            Customer.objects.create(user=form.username, email = user.email)
            
            messages.success(request, 'Account was created for ' +username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'accounts/register.html',context)

@unauthenticated_user
def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return render(request, 'accounts/login.html')
    
    return render(request, 'accounts/login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')