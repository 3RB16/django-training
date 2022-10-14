from django.contrib import admin
from .models import Artist
# Register your models here.

class ArtistDataAdmin(admin.ModelAdmin):
    list_display = ('stage_name' , 'social_link' , 'count_albums')

admin.site.register(Artist, ArtistDataAdmin)
