import json

import pandas as pd
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate

from recommendations.utils import DataLoadingCleaningUtils
from recommendations.views import RecommendationList


class RecommendationsTest(APITestCase):

    def setUp(self):
        self.game_results = {
            "Adrian": ["Gears of War 4", "Madden NFL 20", "NBA 2K20"],
            "Vladimir": ["Uncharted 4"],
            "Naveen": ["FIFA 20", "XCOM 2"],
            "Mitsuki": ["Uncharted 4", "Need for Speed: Heat", "F1 2019", "The Last of Us"],
            "Olivier": [],
            "Roberto": ["FIFA 20", "XCOM 2", "PUBG", "Gran Turismo Sport", "Project CARS 2", "Farenheit", "F1 2019",
                        "The Crew 2"],
            "Sharzad": ["FIFA 20", "PUBG", "Madden NFL 20"],
            "Xi": ["Killzone Shadowfall", "XCOM 2", "PUBG", "Need for Speed: Heat",
                   "Gran Turismo Sport", "F1 2019"],
        }

    @classmethod
    def setUpTestData(cls):
        xls = pd.ExcelFile('data_tables.xlsx')
        game_sheet = pd.read_excel(xls, 'Games')
        user_sheet = pd.read_excel(xls, 'Users')
        attribute_sheet = pd.read_excel(xls, 'Attributes')
        util = DataLoadingCleaningUtils()
        util.add_games(game_sheet)
        util.add_attributes(attribute_sheet)
        util.add_users(user_sheet)

    def test_recommendations(self):
        factory = APIRequestFactory()
        users = User.objects.all()
        for user in users:
            view = RecommendationList.as_view()
            request = factory.get('/api/recommend/', content_type='application/json')
            force_authenticate(request, user=user)
            response = view(request)
            result = json.loads(response.content)
            res = self.checkEqual(result, self.game_results[user.first_name])
            self.assertTrue(res)

    def checkEqual(self, L1, L2):
        return len(L1) == len(L2) and sorted(L1) == sorted(L2)

