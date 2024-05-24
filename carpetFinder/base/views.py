from django.shortcuts import render, redirect
from carpet.models import Carpet
from .forms import SignupForm
from django.contrib.auth import logout

def home(request):
    carpets = Carpet.objects.filter(is_sold=False)[0:6]
    return render(request, 'base/index.html', {
        'carpets': carpets
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'base/signup.html', {
        'form': form
    })

def _logout(request):
    logout(request)
    return redirect('base:home')