from collections import defaultdict

from django.contrib.auth.models import User
import pandas as pd

from recommendations.models import Games, Attributes, Profile

class Utility:

    def add_games(self, game_sheet):
        Games.objects.all().delete()
        for e in game_sheet.T.to_dict().values():
            age = int(''.join(filter(str.isdigit, e['Target Age Group'])))
            violence = "Absent" if e['Game Category: Violence'] == 'None' else e['Game Category: Violence']
            Games.objects.create(name=e['Game Name'],
                                 cover_url=e['Cover URL'],
                                 age_group=age,
                                 theme=e['Game Category: Theme'],
                                 genre=e['Game Category: Genre'],
                                 violence=violence)

    def add_attributes(self, attr_sheet):
        Attributes.objects.all().delete()
        result = defaultdict(list)
        attr_sheet.replace('None', 'Absent', inplace=True)
        # print(attr_sheet.to_dict())
        for key, values in attr_sheet.to_dict().items():
            for k, v in values.items():
                # print(v, type(v))
                if not pd.isnull(v):
                    result[key.lower()].append(v)
        Attributes.objects.create(attributes=result)

    def add_users(self, user_sheet):
        Profile.objects.all().delete()
        User.objects.all().exclude(username="admin").delete()

        for e in user_sheet.T.to_dict().values():
            attrs = Attributes.objects.all().first()
            attrs = attrs.attributes
            themes = attrs.get('themes')
            genres = attrs.get('genres')
            violence = attrs.get('violence')

            result = {}
            val = "Doesn't Matter"
            result['theme'] = [x.strip() for x in e['Game Category: Theme'].split(',')]
            result['theme'] = themes if result['theme'][0].lower() == val.lower() else result['theme']
            result['theme'] = ["Absent" if value == "None" else value for value in result['theme']]

            result['genre'] = [x.strip() for x in e['Game Category: Genres'].split(',')]
            result['genre'] = genres if result['genre'][0].lower() == val.lower() else result['genre']
            result['genre'] = ["Absent" if value == "None" else value for value in result['genre']]

            result['violence'] = [x.strip() for x in e['Game Category: Violence'].split(',')]
            result['violence'] = violence if result['violence'][0].lower() == val.lower() else result['violence']
            result['violence'] = ["Absent" if value == "None" else value for value in result['violence']]

            # print(e['Name'],result)
            user = User.objects.create_user(username=e['Name'],
                                            first_name=e['Name'],
                                            email=e['Name'].lower() + '@estore.com',
                                            password='password')
            Profile.objects.create(user=user,
                                   age=e['Age'],
                                   preferences=result)
