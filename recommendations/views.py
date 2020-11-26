from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
# finds which user is logged in
# write unoptimized query which returns data abased on age and attributes

# create a login API for a user
from rest_framework import viewsets, permissions, authentication, status
from rest_framework.response import Response
from rest_framework.views import APIView

from recommendations.models import Profile, Games
from recommendations.serializers import ProfileSerializer, GamesSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class GamesViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    permission_classes = [permissions.IsAuthenticated]


class RecommendationList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # get the profile
        # get the games according to the users according to age and then filter by genere, theme and violence
        user_object = request.user
        profile = Profile.objects.get(user=user_object)
        games = Games.objects.get()
        return Response(profile.age)
