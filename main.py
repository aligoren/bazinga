from weppy import App, session, redirect, url, response, request
from weppy.sessions import SessionManager, current
from weppy.tools import service

from weppy.orm import Database
from weppy.tools import Auth, requires
from models.Models import User, Issue

app = App(__name__)
app.config.db.uri = 'postgres://ali:ali@localhost/bazinga'

app.config.auth.single_template = True
app.config.auth.registration_verification = False
app.config.auth.hmac_key = "SomedayWholePeopleWillbeFucked"

db = Database(app, auto_migrate=True)
auth = Auth(app, db, user_model=User)

app.pipeline = [
    SessionManager.cookies('SomedayWholePeopleWillbeFucked'),
    db.pipe,
    auth.pipe
]

db.define_models(User, Issue)

auth_routes = auth.module(__name__)

def not_authorized():
    redirect(location='/system/login', status_code=302)

@app.route('/', methods=["get"], template='pages/index.html')
def index():
    response.meta.title = 'Bazinga Issue Tracker System'

    return dict(user={})


@app.route('/me', methods=['get'], template='pages/me.html')
@requires(auth.is_logged, not_authorized)
def me():
    response.meta.title = 'My profile'

    return dict(me=current.session.auth)

@app.route('/issues/my', methods=['get'], template="pages/issues/my.html")
def my_issues():
    issues = db.where(Issue.user == current.session.auth.user.id).select()

    return dict(issues=issues)

@app.route('/system/login', methods=['get'], template='system/login.html')
def login():
    response.meta.title = "Bazinga Login"
    

@app.route('/system/register', methods=['get'], template='system/register.html')
def register():
    response.meta.title = "Bazinga Register"

@app.route('/system/logout', methods=['get'])
def logout():
    current.session.auth.expiration = -1
    redirect(location='/system/login', status_code=302)



@app.route('/v1/register', methods=['post'])
@service.json
def register_service():
    name = request.params.name
    surname = request.params.surname
    user_email = request.params.user_email
    password = request.params.password

    user = User.create(
        email=user_email,
        password=password,
        first_name=name,
        last_name=surname
    )

    auth.add_membership('member', user)

    isRegister = False

    if user.id > 0:
        isRegister = True

    db.commit()

    data = [{'success': isRegister}]

    return dict(data=data)


@app.route('/v1/login', methods=['post'])
@service.json
def login_service():
    user_email = request.params.user_email
    password = request.params.password

    user = auth.login(user_email, password)

    if user:
        current.session.auth.expiration = 604800 # seconds in a week

    return dict(data=user)

if __name__ == '__main__':
    app.run()