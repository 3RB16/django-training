from django.contrib import admin
from .models import Album , Song
# Register your models here.

class InlineSong(admin.StackedInline):
    model = Song
    extra = 0
    min_num = 1

class AlbumDataAdmin(admin.ModelAdmin):
    inlines = [InlineSong]
    readonly_fields = ('creation_date',)

admin.site.register(Album , AlbumDataAdmin)
admin.site.register(Song)
