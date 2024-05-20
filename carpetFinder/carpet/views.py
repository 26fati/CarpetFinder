from django.shortcuts import render, get_object_or_404, redirect
from .models import Carpet
from .forms import NewCarpetForm, EditCarpetForm

def add(request):
    if request.method == 'POST':
        form = NewCarpetForm(request.POST, request.FILES)

        if form.is_valid():
            carpet = form.save(commit=False)
            carpet.seller = request.user
            carpet.save()

            return redirect('base:home')
    else:
        form = NewCarpetForm()

    return render(request, 'carpet/add.html', {
        'form': form,
        'title': 'New carpet'
    })


def edit(request, id):
    carpet = get_object_or_404(Carpet, id=id, seller=request.user)

    if request.method == 'POST':
        form = EditCarpetForm(request.POST, request.FILES, instance=carpet)

        if form.is_valid():
            form.save()

    else:
        form = EditCarpetForm(instance=carpet)


def delete(request, id):
    carpet = get_object_or_404(Carpet, id=id, seller=request.user)
    carpet.delete()





def get_by_id(request, id):
    carpet = get_object_or_404(Carpet, id=id)