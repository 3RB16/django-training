from django.db import models
from artists.models import Artist
# Create your models here.

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete = models.CASCADE, null = False)
    name = models.CharField(default = 'New Album', max_length = 100, blank = True)
    creation_date = models.DateTimeField(auto_now_add = True)
    release_date = models.DateTimeField(null = False, blank = False)
    cost = models.DecimalField(decimal_places = 2, max_digits = 18, blank = False, null = False)
    
    def __str__(self):
        return self.name