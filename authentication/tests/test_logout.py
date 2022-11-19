import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_logout_success(client):
    response = client.post('/authentication/logout', {}, format='json')
    assert response.status_code == 401
