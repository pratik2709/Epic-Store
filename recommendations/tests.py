import json
from collections import defaultdict

import numpy
import pandas as pd

from django.contrib.auth.models import User
from django.core import management

from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from recommendations.models import Games, Attributes, Profile
from recommendations.utils import Utility
from recommendations.views import RecommendationList


class CreateNewPuppyTest(APITestCase):

    def setUp(self):
        pass

    @classmethod
    def setUpTestData(cls):
        xls = pd.ExcelFile('data_tables.xlsx')
        game_sheet = pd.read_excel(xls, 'Games')
        user_sheet = pd.read_excel(xls, 'Users')
        attribute_sheet = pd.read_excel(xls, 'Attributes')
        util = Utility()
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
            print(user.first_name, json.loads(response.content))


