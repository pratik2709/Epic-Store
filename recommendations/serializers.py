from rest_framework import serializers


class RecommendationSerializer(serializers.Serializer):
    name = serializers.StringRelatedField()
    cover_url = serializers.StringRelatedField()

class BuyGamesSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()