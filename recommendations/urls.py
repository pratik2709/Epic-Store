from django.urls import path

from recommendations.views import RecommendationList

app_name = "recommendations"
urlpatterns = [
    path('recommend/', RecommendationList.as_view()),
]