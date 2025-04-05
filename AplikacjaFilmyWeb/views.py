from django.shortcuts import render, get_object_or_404, redirect
from .models import Film
from .forms import FilmForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def get_all_films(request):
    films = Film.objects.all()
    return render(request, 'all.html', {"films":films})

@login_required(login_url="user_login")
def add_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(get_all_films)

    return render(request, 'add.html', {'form': form})

@login_required(login_url="user_login")
def edit_film(request, id):
    film = get_object_or_404(Film, pk=id)
    form = FilmForm(request.POST or None, request.FILES or None, instance=film)

    if form.is_valid():
        form.save()
        return redirect(get_all_films)

    return render(request, 'edit.html', {'form':form})

@login_required(login_url="user_login")
def delete_film(request, id):
    film = get_object_or_404(Film, pk=id)

    if request.method == "POST":
        film.delete()
        return redirect(get_all_films)

    return render(request, 'delete.html', {'film':film})