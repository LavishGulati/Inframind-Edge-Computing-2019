from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *

def home(request):
    if request.method == 'GET':
        return render(request, 'home/home.html', {
            'message': '',
        })
    elif request.method == 'POST':
        form = BillingStartForm(request.POST)
        if form.is_valid():
            contact = form.cleaned_data['Contact']
            NewUser = User(Contact=contact)
            if NewUser is not None:
                return redirect('billing/'+contact)
            else:
                return render(request, 'home/home.html', {
                    'message': 'User not found. Register if new user.'
                })
        else:
            return render(request, 'home/home.html', {
                'message': 'Fill the contact of the person'
            })

def billing(request, contact):
    if request.method == 'GET':
        return render(request, 'home/billing.html')
    elif request.method == 'POST':
        pass

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'home/register.html', {
            'message': '',
        })
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
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
