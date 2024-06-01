from django.shortcuts import render, redirect
from carpet.models import Carpet
from .forms import SignupForm
from django.contrib.auth import logout, login
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import LoginForm



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

@login_required
def search(request):
    query = request.GET.get('q', '')
    style = request.GET.get('style')
    color = request.GET.get('color')
    suitability = request.GET.get('suitability')
    carpets = Carpet.objects.filter(is_sold=False)
    if query:
        carpets = carpets.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(location__icontains=query))

    if style:
        carpets = carpets.filter(style=style)
    if color:
        carpets = carpets.filter(color=color)
    if suitability:
        carpets = carpets.filter(suitability=suitability)

    styles = [style[0] for style in Carpet.STYLE_CHOICES]
    colors = [color[0] for color in Carpet.COLOR_CHOICES]
    suitabilities = [suitability[0] for suitability in Carpet.SUITABILITY_CHOICES]

    return render(request, 'base/search.html', {
        'query': query,
        'carpets': carpets,
        'styles': styles,
        'colors': colors,
        'suitabilities': suitabilities
    })

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
                user = form.get_user()
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('base:index')
    else:
        form = LoginForm()
    return render(request, 'base/login.html', {'form': form})


def profile(request):
    user_profile = request.user
    return render(request, 'base/profile.html', {
        'user_profile': user_profile
    })