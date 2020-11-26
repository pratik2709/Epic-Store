from django.shortcuts import render

# Create your views here.
# finds which user is logged in
# write unoptimized query which returns data abased on age and attributes

# create a login API for a user
from rest_framework import viewsets, permissions
from recommendations.models import Profile
from recommendations.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]