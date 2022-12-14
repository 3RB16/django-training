from django.db import models
from artists.models import Artist
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django import forms
from django.dispatch import receiver
from django.utils.text import slugify
from .tasks import send_mail_task
from django.db.models.signals import post_save, pre_save

from .validators import audio_file_validator


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete = models.CASCADE, null = False)
    name = models.CharField(default = 'New Album', max_length = 100, blank = True)
    creation_date = models.DateTimeField(auto_now_add = True)
    release_date = models.DateTimeField(null = False, blank = False)
    cost = models.DecimalField(decimal_places = 2, max_digits = 18, blank = False, null = False)
    is_approved = models.BooleanField(default = False , help_text = " Approve the album if its name is not explicit")    

    class Meta:
        db_table = 'albums'

    def __str__(self):
        return self.name



class Song (models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE,related_name="songs")
    name = models.CharField(max_length=200 , blank = True)
    image = models.ImageField(blank=False, null=False)
    thumbnail = ImageSpecField(source='image',
                                processors=[ResizeToFill(100, 50)],
                                format='JPEG',
                                options={'quality': 60}
                            )
    audio_file = models.FileField(upload_to='musics/' , validators=[audio_file_validator])

    def __str__(self):
            return self.name + " Song, in " + self.album.name + " Album "

    def clean(self):
        if self.name == "":
            self.name = self.album.name

    def delete(self, *args, **kwargs): 
        if (self.album.song_set.all().count() > 1):
            super(Song, self).delete(*args, **kwargs)
        else:
            raise forms.ValidationError("Can't be deleted")

@receiver(post_save, sender=Album)
def album_post_save(sender, instance, created, *args, **kwargs):
    if created:
        send_mail_task.delay(instance.name, instance.artist.id)


@receiver(pre_save, sender=Song)
def song_pre_save(sender, instance, *args, **kwargs):
    if len(instance.name.strip()) == 0:
        instance.name = slugify(instance.album.name)

