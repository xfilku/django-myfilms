from django.db import models

class AdditionalInfo(models.Model):
    CATEGORIES = {
        (0, 'Inne'),
        (1, 'Horror'),
        (2, 'Komedia'),
        (3, 'Sci-fi'),
        (4, 'Dramat'),
    }

    time = models.PositiveSmallIntegerField(default=0)
    category = models.PositiveSmallIntegerField(default=0, choices=CATEGORIES)

class Film(models.Model):
    title = models.CharField(max_length=50, null=True, blank=False)
    description = models.TextField(max_length=500, blank=True)
    year = models.PositiveIntegerField(default=2014)
    poster = models.ImageField(blank=True, upload_to='posters')
    additional = models.OneToOneField(AdditionalInfo, on_delete=models.CASCADE, null=True, blank=True) # jeden do jednego | gdy usuwamy tą relacje CASCADE usuwa tez ten opis dla tego filmu

    def __str__(self):
        return "{} ({})".format(self.title, self.year)
    
class Rating(models.Model):
    rating = models.DecimalField(decimal_places=2, max_digits=4, default=10.00)
    description = models.TextField(max_length=300)
    film = models.ForeignKey(Film, on_delete=models.CASCADE) #wiele do jednego

    def __str__(self):
        return "{} {}".format(self.film, self.rating)
    
class Actor(models.Model):
    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=54)
    film = models.ManyToManyField(Film) #wiele do wielu

    def __str__(self):
        return "{} {}".format(self.name, self.last_name)
