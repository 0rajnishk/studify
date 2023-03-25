from flask import Flask, flash, render_template, request, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
from werkzeug.middleware.proxy_fix import ProxyFix

import os
import secrets
from datetime import timedelta

from course import course
from utils import login_required


# App config
app = Flask(__name__)
app.register_blueprint(course)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)


# Session config
app.secret_key = secrets.token_hex(16)
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)
# Allow session cookies to be cleared by JavaScript
app.config['SESSION_COOKIE_HTTPONLY'] = False
app.config['SESSION_COOKIE_SECURE'] = False
# The above two lines should be removed ========================================
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
    client_kwargs={'scope': 'email profile'},
    validate_token=True,  # enable token validation
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration'
)


# routes

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    redirect_uri = url_for('oauth_callback', _external=True, _scheme=request.scheme)
    return google.authorize_redirect(redirect_uri)


# Define a list of allowed domains
allowed_domains = ['ds.study.iitm.ac.in',
                   'study.iitm.ac.in', 'ds.study.iitm.ac.in']

# Define a list of blocked emails
blocked_emails = ['user@example.com']

# Define a list of admin emails
admin_emails = ['surajnish02@gmail.com', 'studify.iitm@gmail.com']


@app.route('/oauth-callback')
def oauth_callback():
    google = oauth.create_client('google')  # create the google oauth client
    # Access token from google (needed to get user info)
    token = google.authorize_access_token()
    # userinfo contains stuff u specified in the scope
    resp = google.get('userinfo')
    user_info = resp.json()
    email = user_info['email']
    domain = email.split('@')[-1]
    if domain in allowed_domains or email in admin_emails:
        if email in blocked_emails:
            return 'You are blocked. Contact admin for more details'
        else:
            session['profile'] = user_info
            email
            session.permanent = True
            return redirect(url_for('course.get_term_metadata', term_id="23t1"))
    else:
        session.pop('profile', None)
        return 'You are not authorized to access this page. Please use student email address.'


@app.route('/logout')
def logout():
    session.pop('profile', None)
    flash('You have been logged out successfully!', 'success')
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
