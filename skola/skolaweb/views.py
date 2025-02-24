from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm
from django.http import HttpResponseRedirect
import time
from skolaweb.models import *
from skolaweb.forms import *
# Create your views here.
def index(request):
    t=time.localtime()
    s='{}:{}:{}'.format(t[3],t[4],t[5])
    podaci={'vrijeme':s}
    return render(request, 'index.html', podaci)
 


def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')

def ucenici_index(request):
    data=Ucenik.objects.all().order_by("Prezime")
    podatci={'data':data}
    return render(request,"ucenici_index.html",podatci)

def ucenici_add(request):
        form=UcenikAdd()
        return render(request, "ucenici_add.html", {'form':form})