from flask import Flask, render_template, request, redirect, url_for, session
from authlib.integrations.flask_client import OAuth

from functools import wraps
import os
import secrets
from datetime import timedelta

# dotenv setup
# from dotenv import load_dotenv
# load_dotenv()

from course import course
# decorator for routes that should be accessible only by logged in users


def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'profile' not in session:
            return redirect(url_for('login', next=request.url))
        email = session['profile']['email']
        if email.endswith('@ds.study.iitm.ac.in'):
            return func(*args, **kwargs)
        else:
            return f'You are not authorized to access this page. Please use an authorized email address ({email}).'
    return decorated_function


# App config
app = Flask(__name__)
app.register_blueprint(course)
# Session config
app.secret_key = secrets.token_hex(16)
app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

# oAuth Setup
oauth = OAuth(app)

# Google configuration
google = oauth.register(
    name='google',
    client_id='42857344288-a6bavno9hc3naf95rfgosfn5op8gts98.apps.googleusercontent.com',
    client_secret='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',

    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
    client_kwargs={'scope': 'openid email profile'},
    validate_token=True  # enable token validation
)


# routes

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return redirect(url_for('authorize'))


@app.route('/authorize')
def authorize():
    redirect_uri = url_for('oauth_callback', _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route('/oauth-callback')
def oauth_callback():
    google = oauth.create_client('google')  # create the google oauth client
    # Access token from google (needed to get user info)
    token = google.authorize_access_token()
    # userinfo contains stuff u specified in the scope
    resp = google.get('userinfo')
    user_info = resp.json()
    if user_info['email'].endswith('@ds.study.iitm.ac.in'):
        session['profile'] = user_info
        # make the session permanent so it keeps existing after the browser gets closed
        session.permanent = True
        return redirect(url_for('hello_world'))
    else:
        return 'You are not authorized to access this page. Please use an authorized email address.'


@app.route('/logout')
def logout():
    session.pop('profile', None)
    return redirect(url_for('index'))


@app.route('/hello-world')
@login_required
def hello_world():
    email = dict(session)['profile']['email']
    return render_template("ind.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
