import pandas as pd
from django.core import management
from django.core.management import BaseCommand

from recommendations.models import Games


class Command(BaseCommand):
    help = 'loads data in the database'

    def handle(self, *args, **options):
        management.call_command('flush')
        df = pd.read_excel("data_tables.xlsx")
        print(df.iloc[0])
        print(df.to_dict())
        print(df.iloc[0]['Game Name'])
        for e in df.T.to_dict().values():
            game = Games.objects.create(name=e['Game Name'],
                                 cover_url=e['Cover URL'],
                                 age_group=e['Target Age Group'],
                                 theme=e['Game Category: Theme'],
                                 genre=e['Game Category: Genre'],
                                 violence=e['Game Category: Violence'])
            print(game)
