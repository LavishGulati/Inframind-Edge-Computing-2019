from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *

def home(request):
    if request.method == 'GET':
        return render(request, 'home/home.html', {
            'message': '',
        })
    elif request.method == 'POST':
        pass

def billing(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass

def register(request):
    if request.method == 'GET':
        form = register_form()
        return render(request, 'home/register.html', {
            'message': '',
        })
    elif request.method == 'POST':
        form = register_form(request.POST)
        if form.is_valid:
            NewUser = User()
            NewUser.Name = form.cleaned_data['Name']
            NewUser.Address = form.cleaned_data['Address']
            NewUser.Contact = form.cleaned_data['Contact']
            NewUser.Email = form.cleaned_data['Email']
            NewUser.save()
            return render(request, 'home/register.html', {
                'message': 'User registration successful',
            })
        else:
            return render(request, 'home/register.html', {
                'message': 'User registration unsuccessful'
            })
