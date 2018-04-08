"""Generated migration

Migration ID: cc3294f75ab8
Revises: ad6d290c5647
Creation Date: 2018-04-08 22:14:04.915287

"""

from weppy.orm import migrations


class Migration(migrations.Migration):
    revision = 'cc3294f75ab8'
    revises = 'ad6d290c5647'

    def up(self):
        self.alter_column('issues', 'user',
            existing_type='reference users',
            type='integer',
            existing_notnull=False)

    def down(self):
        self.alter_column('issues', 'user',
            existing_type='integer',
            type='reference users',
            existing_notnull=False)