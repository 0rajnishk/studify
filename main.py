from flask import Flask, flash, render_template, request, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
from werkzeug.middleware.proxy_fix import ProxyFix

import os
import re
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
    next_url = request.args.get('next', None)
    if next_url and 'http://127.0.0.1:5000/pyq' in next_url:
        next_url = 'pyq'
    elif next_url and '23t1' in next_url:
        next_url = 'term/23t1'
    elif next_url and '23q1' in next_url:
        next_url = 'term/23q1'
    print(next_url,"\n\n\n\n\n\n\n")
    redirect_uri = url_for('oauth_callback', _external=True, _scheme=request.scheme, next=next_url)
    return google.authorize_redirect(redirect_uri)



# Define a list of allowed domains
allowed_domains = ['ds.study.iitm.ac.in',
                   'study.iitm.ac.in', 'ds.study.iitm.ac.in']

# Define a list of blocked emails
blocked_emails = ['user@example.com']

# Define a list of admin emails
admin_emails = ['surajnish02@gmail.com',
                'studify.iitm@gmail.com', 'studify.dummy@gmail.com']

@app.route('/oauth-callback')
def oauth_callback():
    try:
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
                next_url = request.args.get('next')
                if next_url and 'http://127.0.0.1:5000/pyq' in next_url:
                    next_url = 'pyq'
                elif next_url and 'term/23t1' in next_url:
                    next_url = 'term/23t1'
                elif next_url and 'term/23q1' in next_url:
                    next_url = 'term/23q1'
                print(next_url,"\n\n\n\n\n\n\n")
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect(url_for('course.get_term_metadata', term_id="23t1"))
        else:
            # if re.match("/course/ns_2[3-9]{1}q[1-3]{1}_[a-z]{2}[0-9]{4}", urlparse(request.url).path):
            # session['profile'] = user_info
            # session.permanent = True
            next_url = request.args.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect(url_for('course.get_term_metadata', term_id="23q1"))

            # session.pop('profile', None)
            # return 'You are not authorized to access this page. Please use student email address.'
    except Exception as e:
        # print(str(e))
        return 'Error: ' + str(e)



@app.route('/logout')
def logout():
    session.pop('profile', None)
    flash('You have been logged out successfully!', 'success')
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
