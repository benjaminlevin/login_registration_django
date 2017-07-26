from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import User, function
from django.core.urlresolvers import reverse

def index(request):
    return render(request, "lrapp/index.html", context)

def create(request):
    if request.method == 'POST':
        if User.objects.validate(request) is False:
            return redirect('/')
        else:
            return redirect('/success')
    return redirect('/')

def login(request):
    if request.method == 'POST':
        if User.objects.login(request) is False:
            return redirect('/')
        elif User.objects.login(request) is True:
            return redirect('/success')
    else:
        return redirect('/')

def success(request):
    return render(request, "lrapp/success.html")

def deletedb(request):
    User.objects.all().delete()
    return redirect('/')