from django.forms import ModelForm
from .models import Film, AdditionalInfo, Rating

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'year', 'poster']

class AdditionalInfoForm(ModelForm):
    class Meta:
        model = AdditionalInfo
        fields = ['time', 'category']

class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['rating', 'description']