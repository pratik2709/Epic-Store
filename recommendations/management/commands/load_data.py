from collections import defaultdict

import numpy
import pandas as pd
from django.contrib.auth.models import User
from django.core.management import BaseCommand

from recommendations.models import Games, Attributes, Profile


class Command(BaseCommand):
    help = 'loads data in the database'

    def handle(self, *args, **options):
        # management.call_command('flush', interactive=False)

        xls = pd.ExcelFile('data_tables.xlsx')
        game_sheet = pd.read_excel(xls, 'Games')
        user_sheet = pd.read_excel(xls, 'Users')
        attribute_sheet = pd.read_excel(xls, 'Attributes')

        self.add_games(game_sheet)
        self.add_attributes(attribute_sheet)
        self.add_users(user_sheet)

    def add_games(self, game_sheet):
        Games.objects.all().delete()
        for e in game_sheet.T.to_dict().values():
            age = int(''.join(filter(str.isdigit, e['Target Age Group'])))
            game = Games.objects.create(name=e['Game Name'],
                                        cover_url=e['Cover URL'],
                                        age_group=age,
                                        theme=e['Game Category: Theme'],
                                        genre=e['Game Category: Genre'],
                                        violence=e['Game Category: Violence'])
            print(game)

    def add_attributes(self, attr_sheet):
        Attributes.objects.all().delete()
        print(attr_sheet.to_dict())
        result = defaultdict(list)
        attr_sheet = attr_sheet.replace({numpy.NaN: None})
        for key, values in attr_sheet.to_dict().items():
            for k, v in values.items():
                result[key].append(v)

        print(result)
        Attributes.objects.create(attributes=result)

    def add_users(self, user_sheet):
        Profile.objects.all().delete()
        User.objects.all().exclude(username="admin").delete()
        print(user_sheet.T.to_dict())

        for e in user_sheet.T.to_dict().values():
            result = dict()
            result = {}
            val = "Doesn't Matter"
            val = val.lower()
            result['theme'] = [x.strip() for x in e['Game Category: Theme'].split(',')]
            result['theme'] = [value for value in result['theme'] if value.lower() != val]

            # result['theme'] = ["Absent" if value == "None" else value for value in result['theme']]

            result['genre'] = [x.strip() for x in e['Game Category: Genres'].split(',')]
            result['genre'] = [value for value in result['genre'] if value.lower() != val]
            # result['genre'] = ["Absent" if value == "None" else value for value in result['genre']]

            result['violence'] = [x.strip() for x in e['Game Category: Violence'].split(',')]
            result['violence'] = [value for value in result['violence'] if value.lower() != val]
            # result['violence'] = ["Absent" if value == "None" else value for value in result['violence']]

            print(result)
            user = User.objects.create_user(username=e['Name'],
                                            first_name=e['Name'],
                                            email=e['Name'].lower() + '@estore.com',
                                            password='password')
            Profile.objects.create(user=user,
                                   age=e['Age'],
                                   preferences=result)
