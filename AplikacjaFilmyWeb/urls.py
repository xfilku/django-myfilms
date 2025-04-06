from django.urls import path
from .views import get_all_films, add_film, edit_film, delete_film, show_film, add_rating
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('all/', get_all_films, name="all_films"),
    path('add/', add_film, name="add_film"),
    path('edit/<int:id>', edit_film, name="edit_film"),
    path('delete/<int:id>', delete_film, name="delete_film"),
    path('film/<int:id>', show_film, name="show_film"),
    path('add_rating/<int:id>', add_rating, name="add_rating")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
