from rest_framework import status
from rest_framework.test import APIClient
import pytest



def validate_response(response, user):
    response_user = response.data['user']
    assert response_user['username'] == user['username']
    assert response_user['email'] == user['email']
    assert response_user['bio'] == user['bio']
    assert 'token' not in response_user
    assert 'token' in response.data
    assert 'id' in response_user
    assert 'password' not in response_user
    

@pytest.mark.django_db
def test_login_success(client):
    
    user = {
        'username' : "Muhammad_arbi",
        'email' : "muhammad3rbi@gmail.com",
        'password1' : "Password1!",
        'password2' : "Password1!",
        "bio" : "software engineer intern at bld.ai"
    }

    # register the user
    response = client.post("/authentication/register/", user)
    assert response.status_code == status.HTTP_201_CREATED

    
    # login the user
    response = client.post("/authentication/register/", {'username' : "Muhammad_arbi", 
    'password' : "Password1!",})
    assert response.status_code == status.HTTP_200_OK      
    validate_response(response, user)


@pytest.mark.django_db
def test_login_fail(client):
        
    # login the user
    response = client.post("/authentication/register/", {'username' : "memo", 'password' : "Password1!",})
    assert response.status_code == status.HTTP_404_NOT_FOUND
