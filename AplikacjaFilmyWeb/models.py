from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=50, null=True, blank=False)
    description = models.TextField(max_length=500, blank=True)
    year = models.PositiveIntegerField(default=2014)
    poster = models.ImageField(blank=True, upload_to='posters')

    def __str__(self):
        return self.title