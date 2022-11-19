import pytest
from users.models import User


@pytest.mark.django_db
def test_login_success (client):
    User.objects.create_user(username="muhammad_arbi", password="123456mo")
    response = client.post('/authentication/login', {"username":"muhammad_arbi","password":"123456mo"}, format='json')
    assert response.status_code == 200

@pytest.mark.django_db
def test_login_fail(client):
    User.objects.create_user(username="muhammad_arbi", password="123456mo")
    response = client.post('/authentication/login', {"username":"muhammad_arbi","password":"123456mo"}, format='json')
    #already logged in
    response = client.post('/authentication/login', {"username":"muhammad_arbi","password":"123456mo"}, format='json')
    assert response.status_code == 403

