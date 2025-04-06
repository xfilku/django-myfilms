from django.shortcuts import render, get_object_or_404, redirect
from .models import Film, AdditionalInfo, Rating
from .forms import FilmForm, AdditionalInfoForm, RatingForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def get_all_films(request):
    films = Film.objects.all()
    return render(request, 'all.html', {"films":films})

@login_required(login_url="user_login")
def add_film(request):
    form_film = FilmForm(request.POST or None, request.FILES or None)
    form_additional_info = AdditionalInfoForm(request.POST or None)

    if form_film.is_valid() and form_additional_info.is_valid():
        film = form_film.save(commit=False)
        additional = form_additional_info.save()
        film.additional = additional
        film.save()
        return redirect(get_all_films)

    return render(request, 'add.html', {'form': form_film, "form_additional_info": form_additional_info})

@login_required(login_url="user_login")
def edit_film(request, id):
    film = get_object_or_404(Film, pk=id)
    additional = None
    try:
        additional = AdditionalInfo.objects.get(film=film.id)
    except AdditionalInfo.DoesNotExist:
        additional = None

    form = FilmForm(request.POST or None, request.FILES or None, instance=film)
    form_additional = AdditionalInfoForm(request.POST or None, instance=additional)

    if form.is_valid() and form_additional.is_valid():
        film = form.save(commit=False)
        additional = form_additional.save()
        film.additional = additional
        film.save()
        return redirect(get_all_films)

    return render(request, 'edit.html', {'form':form, 'form_additional_info':form_additional})

@login_required(login_url="user_login")
def delete_film(request, id):
    film = get_object_or_404(Film, pk=id)

    if request.method == "POST":
        film.delete()
        return redirect(get_all_films)

    return render(request, 'delete.html', {'film':film})

def show_film(request, id):
    film = get_object_or_404(Film, pk=id)
    ratings = None
    try:
        ratings = Rating.objects.filter(film = film)
    except Rating.DoesNotExist:
        ratings = None

    return render(request, 'film.html', {"film":film, 'ratings':ratings})

@login_required(login_url="user_login")
def add_rating(request, id):
    pass
#     rating_form = RatingForm(request.POST or None)

#     if rating_form.is_valid():
#         rating_form.save()

#     return render(request=)