import itertools

from django.db.models import Q
from django.http import JsonResponse
from rest_framework import permissions, generics, authentication, status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response

from recommendations.models import Profile, Games
from recommendations.serializers import RecommendationSerializer, BuyGamesSerializer


class RecommendationList(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RecommendationSerializer
    http_method_names = ['get']

    def list(self, request):
        queryset = self.get_queryset(request)
        return JsonResponse(list(queryset.values_list('name', flat=True)), safe=False)

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


class BuyGamesView(ListModelMixin, CreateModelMixin, GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BuyGamesSerializer
    queryset = Profile.objects.all()

    def post(self, request, *args, **kwargs):
        # skipping actual creation of object due to time constraints
        serializer = self.get_serializer(data=request.data, many=True)
        print(request.data)
        return Response("Successfully created", status=status.HTTP_201_CREATED)




