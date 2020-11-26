from django.contrib.auth.models import User
from rest_framework import serializers

from recommendations.models import Profile, Games


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['user', 'age', 'preferences']

class GamesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Games
        fields = ['name', 'age_group', 'theme', 'genre', 'violence']
