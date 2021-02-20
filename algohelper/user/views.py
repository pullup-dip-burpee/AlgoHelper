from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import IntegrityError
from user.serializers import UserSerializer
from rest_framework.authtoken.models import Token
import requests

# API User==================================================================
# POST /users/
# GET /users/
# PUT /users/signin/
# GET /users/me/
# PUT /users/me/
# GET /users/{user_id}/
# GET /users/profile/

class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # GET /users/
    def list(self, request):
        return_data = UserSerializer(self.queryset, many=True).data
        return Response(data=return_data)

    # POST /users/
    def create(self, request):
        return Response()

    # GET /users/me/
    def retrieve(self, request, pk=None):
        return Response()

    # PUT /users/me/
    def update(self, request, pk=None):
        return Response()