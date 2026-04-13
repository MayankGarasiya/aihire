from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserMeSerializer


class EmailTokenObtainPairView(TokenObtainPairView):
    """
    Uses SimpleJWT default serializer; our User model uses email as USERNAME_FIELD,
    so clients post { "email": "...", "password": "..." }.
    """


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserMeSerializer(request.user).data)

from django.shortcuts import render

# Create your views here.
