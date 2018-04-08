from weppy import session, now
from weppy.orm import Field, Model, belongs_to, has_many
from weppy.tools.auth import AuthUser

class User(AuthUser):
    has_many('issues')


class Issue(Model):

    belongs_to('user')

    title = Field()
    date = Field.datetime()
    user = Field.int

    default_values = {
        'user': lambda: session.auth.user.id,
        'date': lambda: now
    }