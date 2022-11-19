from django.urls import path , include
from .views import ArtistView

urlpatterns = [
    path('' , ArtistView.as_view() , name="artists"),
]
