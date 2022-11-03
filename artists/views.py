from imaplib import _Authenticator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated , AllowAny

from .serializers import ArtistSerializer
from .models import Artist

class ArtistView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self , request):
        serializer = ArtistSerializer(Artist.objects.all() , many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self , request):
        serializer = ArtistSerializer(data = request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST) 