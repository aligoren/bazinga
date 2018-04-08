"""Generated migration

Migration ID: 520e6a302a76
Revises: cc3294f75ab8
Creation Date: 2018-04-08 22:43:52.545245

"""

from weppy.orm import migrations


class Migration(migrations.Migration):
    revision = '520e6a302a76'
    revises = 'cc3294f75ab8'

    def up(self):
        self.alter_column('issues', 'user',
            existing_type='integer',
            type='reference users',
            existing_notnull=False)

    def down(self):
        self.alter_column('issues', 'user',
            existing_type='reference users',
            type='integer',
            existing_notnull=False)