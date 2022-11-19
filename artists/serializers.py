from dataclasses import field
from rest_framework import serializers
from .models import Artist

class ArtistSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    stage_name = serializers.CharField(max_length = 100, allow_blank = False)
    social_link = serializers.URLField(max_length = 200, required=True , allow_blank = True)

    class Meta:
        model = Artist
        fields = '__all__'
