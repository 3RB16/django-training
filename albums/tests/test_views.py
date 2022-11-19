import pytest
import json
from artists.models import Artist
from albums.models import Album
from albums.serializers import AlbumSerializer
from users.models import User

@pytest.mark.django_db
def test_get_albums(client):
    user = User.objects.create_user(username="muhammad",password="123456mo")
    artist1 = Artist.objects.create(stage_name="arbi",user=user)
    artist2 = Artist.objects.create(stage_name="memo",social_link="https://google.com")
    Album.objects.create(name="test1",release_datetime="2022-2-2 12:12" ,cost=2,is_approved=True,artist=artist1)
    Album.objects.create(name="test2",release_datetime="2022-1-2 12:12" ,cost=122,is_approved=True,artist=artist1)
    Album.objects.create(release_datetime="2021-2-2 12:12" ,cost=12,artist=artist2)
    response = client.get('/albums/')
    assert response.status_code == 200
    response_content = json.loads(response.content.decode("unicode_escape"))
    serializer = AlbumSerializer(Album.objects.filter(is_approved=True),many=True)
    expected_response_content = serializer.data
    assert response_content["results"] == expected_response_content
    

@pytest.mark.django_db
def test_get_albums_with_filter(client):
    user = User.objects.create_user(username="muhammad",password="123456mo")
    artist1 = Artist.objects.create(stage_name="arbi",user=user)
    artist2 = Artist.objects.create(stage_name="memo",social_link="https://google.com")
    Album.objects.create(name="test1",release_datetime="2022-2-2 12:12" ,cost=2,is_approved=True,artist=artist1)
    Album.objects.create(name="test2",release_datetime="2022-1-2 12:12" ,cost=122,is_approved=True,artist=artist1)
    Album.objects.create(release_datetime="2021-2-2 12:12" ,cost=12,artist=artist2)
    response = client.get('/albums/?cost__gte=10')
    assert response.status_code == 200
    response_content = json.loads(response.content.decode("unicode_escape"))
    serializer = AlbumSerializer(Album.objects.filter(is_approved=True,cost__gte=10),many=True)
    expected_response_content = serializer.data
    assert response_content["results"] == expected_response_content
    

@pytest.mark.django_db
def test_post_no_auth(client):
    response = client.post('/albums/', {"name":"muhammad","release_datetime":"2011-12-12 10:10","cost":3},format="json")
    assert response.status_code == 401
    response_content = json.loads(response.content.decode("unicode_escape"))
    expected_response_content = {"detail":"Authentication credentials were not provided."}
    assert response_content == expected_response_content
    


@pytest.mark.django_db
def test_post_user_not_artist(client):
    user = User.objects.create_user(username="muhammad", password="123456mo")
    response = client.post('/albums/', {"name":"arbi","release_datetime":"2011-12-12 10:10","cost":3},format="json")
    assert response.status_code == 403
    response_content = json.loads(response.content.decode("unicode_escape"))
    expected_response_content = {"detail":"you must be an artist to do this request"}
    assert response_content == expected_response_content


@pytest.mark.django_db
def test_post(client):
    user = User.objects.create_user(username="muhammad", password="123456mo")
    Artist.objects.create(stage_name="memo",user=user)
    response = client.post('/albums/', {"name":"arbi","release_datetime":"2011-12-12 10:10","cost":3},format="json")
    assert response.status_code == 201
    response_content = json.loads(response.content.decode("unicode_escape"))
    expected_response_content = {"message":"album created"}
    assert response_content == expected_response_content
    
