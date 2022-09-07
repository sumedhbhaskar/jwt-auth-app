from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import CreateAPIView,GenericAPIView, ListAPIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

from user.models import CustomUser
from .serializers import LoginSerializer, SignUpSerializers, ListUserSerilier


class SignUpView(CreateAPIView):



    serializer_class = SignUpSerializers
    queryset = CustomUser.objects.all()

class LoginView(GenericAPIView):

    serializer_class = LoginSerializer
    queryset = CustomUser.objects.all()

    def post(self,request,*args,**kwargs):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username,password=password)

        if not user:
            raise ValueError("No user found!")

        refresh_token = RefreshToken.for_user(user) 
        access_token = str(refresh_token.access_token)
        refresh_token = str(refresh_token)

        return Response(
            {
                "Username":username,
                "Access token":access_token,
                "Refresh token":refresh_token
            },
            status=status.HTTP_200_OK
        )


class CheckAuthentication(ListAPIView):

    serializer_class = ListUserSerilier
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated,]

        




