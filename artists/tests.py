from django.test import TestCase,RequestFactory
from .models import Artist  
from .views import ArtistsView
from .serializers import ArtistSerializer

class ArtistTests(TestCase):
    def setUp(self):
        Artist.objects.create(stage_name="arbi",social_link="http:3RB")

    def test_insert(self):  
        artist1 = ArtistSerializer(Artist.objects.get(id=1))
        self.assertEqual(artist1.data,{"id":1,"stage_name":"arbi","social_link":"http:3RB","albums":[]}) 

    def test_get_all(self):
        request = RequestFactory().get('/artists/')
        response = ArtistsView.as_view()(request)
        all_artists = ArtistSerializer(Artist.objects.all().prefetch_related("albums"),many=True)
        self.assertEqual(all_artists.data,response.data)
