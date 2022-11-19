from rest_framework import serializers
from .models import User
from .validators import validate_username

class UserSerializer (serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    bio = serializers.CharField(max_length=256)

    class Meta:
        model = User
        fields=("id","username","email","bio")
