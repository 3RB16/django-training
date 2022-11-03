from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import AlbumSerializer
from .models import Album


class AlbumView(APIView):
    def get(self , request):
        serializer = AlbumSerializer(Album.objects.all() , many = True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def post(self , request):
        serializer = AlbumSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)