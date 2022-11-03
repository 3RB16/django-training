from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsAuthenticated,IsSuperUser
from .serializers import RegisterUserSerializer ,GetUserSerializer
from users.models import User
from django.contrib.auth import authenticate, login ,logout
from knox.views import LoginView as KnoxLoginView
from knox.views import LogoutView as KnoxLogOutView
from knox.models import AuthToken
from knox.auth import TokenAuthentication

class Register (APIView):
    permission_classes=[~IsAuthenticated | IsSuperUser]
    def post (self,request):
        serializer = RegisterUserSerializer(data = request.data)
        if not serializer.is_valid():
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        
        User.objects.create_user(   
            username=serializer.data["username"],
            email=serializer.data["email"],
            password=serializer.data["password1"]
        )
        return Response({"message" : "user created successfully"} , status=status.HTTP_201_CREATED)


class Login (KnoxLoginView):
    permission_classes=[~IsAuthenticated]
    def post (self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            serializer = GetUserSerializer(user)
            token_ttl = self.get_token_ttl()
            instance, token = AuthToken.objects.create(user, token_ttl)
            content = {
                "token":token,
                "user":serializer.data
            }
            return Response(content , status=status.HTTP_200_OK)
        return Response({"message" : "invalid login" }, status=status.HTTP_400_BAD_REQUEST)


class LogOut (KnoxLogOutView):
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def post (self,request):
        logout(request)
        return super(LogOut, self).post(request, format=None)
