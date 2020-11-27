from django.urls import path

from recommendations.views import RecommendationList, BuyGamesView

app_name = "recommendations"
urlpatterns = [
    path('recommend/', RecommendationList.as_view()),
    path('buy/<int:pk>/', BuyGamesView.as_view()),
]