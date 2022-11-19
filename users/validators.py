from .serializers import serializers
from .models import User

def validate_username(self, username):
    existing = User.objects.filter(username=username).first()
    if existing:
        raise serializers.ValidationError("Your username is already in use")
    return username
