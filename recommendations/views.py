import itertools

from django.db.models import Q
# create a login API for a user
from rest_framework import permissions, generics, authentication
from rest_framework.response import Response

from recommendations.models import Profile, Games
from recommendations.serializers import RecommendationSerializer


class RecommendationList(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RecommendationSerializer
    http_method_names = ['get']

    def list(self, request):
        queryset = self.get_queryset(request)
        serializer = RecommendationSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self, request):
        user_object = request.user
        profile = Profile.objects.get(user=user_object)
        profile_preferences = profile.preferences
        profile_violence = profile_preferences.get('violence')
        profile_genres = profile_preferences.get('genre')
        profile_themes = profile_preferences.get('theme')
        games_by_age = Games.objects.filter(age_group__lte=profile.age)
        combinations = list(itertools.product(profile_themes, profile_genres, profile_violence))
        query = Q()
        for theme, genre, violence in combinations:
            query = query | Q(theme=theme, genre=genre, violence=violence)
        res = games_by_age.filter(query)
        return res

# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
# class GamesViewSet(viewsets.ModelViewSet):
#     queryset = Games.objects.all()
#     serializer_class = GamesSerializer
#     permission_classes = [permissions.IsAuthenticated]



