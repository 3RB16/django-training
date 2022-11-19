import pytest
from users.models import User

@pytest.mark.django_db
def test_register_success(client):
    response =  client.post('/authentication/register', {"username":"muhammad_arbi","password1":"aaa12345","password2":"aaa12345"}, format='json')
    assert response.status_code == 400

    response =  client.post('/authentication/register', {}, format='json')
    assert response.status_code == 400

    response = client.post('/authentication/register', {"username":"muhammad_arbi","password1":"123456mo","password2":"123456mo","email":"muhammad_arbi@gmail.com"}, format='json')
    assert response.status_code == 201

@pytest.mark.django_db
def test_register_fail(client):
    response = client.post('/authentication/register', {"username":"muhammad_arbi","password1":"123456aa","password2":"123456aa"}, format='json')
    assert response.status_code == 400

    response = client.post('/authentication/register', {}, format='json')
    assert response.status_code == 400

    response = client.post('/authentication/register', {"username":"muhammad_arbi","password1":"123456mo","password2":"123456mo","email":"muhammad_arbi@gmail.com"}, format='json')
    assert response.status_code == 201

    #user name already in use
    response = client.post('/authentication/register', {"username":"muhammad_arbi","password1":"123456mo","password2":"123456mo","email":"muhammad_arbi@gmail.com"}, format='json')
    assert response.status_code == 400
    
    #already logged in
    response = client.post('/authentication/register', {"username":"muhammad_arbi","password1":"123456mo","password2":"123456mo","email":"muhammad_arbi@gmail.com"}, format='json')
    assert response.status_code == 400
