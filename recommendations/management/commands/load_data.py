import pandas as pd
from django.core.management import BaseCommand

from recommendations.utils import Utility


class Command(BaseCommand):
    help = 'loads data in the database'

    def handle(self, *args, **options):
        # management.call_command('flush', interactive=False)

        xls = pd.ExcelFile('data_tables.xlsx')
        game_sheet = pd.read_excel(xls, 'Games')
        user_sheet = pd.read_excel(xls, 'Users')
        attribute_sheet = pd.read_excel(xls, 'Attributes')
        util = Utility()
        util.add_games(game_sheet)
        util.add_attributes(attribute_sheet)
        util.add_users(user_sheet)

