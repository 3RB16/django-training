from django.contrib import admin
from .models import Artist
from albums.models import Album

# Register your models here.
class AlbumDataAdmin(admin.StackedInline):
    model = Album
    extra = 0

class ArtistDataAdmin(admin.ModelAdmin):
    inlines = [AlbumDataAdmin]
    list_display = ['stage_name' , 'social_link' , 'count_albums']

admin.site.register(Artist, ArtistDataAdmin)
