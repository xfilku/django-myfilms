from django.contrib import admin
from .models import Film, AdditionalInfo, Rating, Actor

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['title', 'year']
    list_filter = ['title', 'year']
    search_fields = ['title', 'description']

@admin.register(AdditionalInfo)
class AdditionalInfoAdmin(admin.ModelAdmin):
    list_display = ['category', 'time']

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['description', 'rating', 'film']

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name']
