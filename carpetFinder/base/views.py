from django.shortcuts import render
from carpet.models import Carpet


def home(request):
    carpets = Carpet.objects.filter(is_sold=False)[0:6]
    return render(request, 'base/index.html', {
        'carpets': carpets
    })