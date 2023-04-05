from functools import wraps
from flask import session, redirect, url_for, request
import re
from urllib.parse import urlparse
# decorator for routes that should be accessible only by logged in users

# Define a list of allowed domains
allowed_domains = ['ds.study.iitm.ac.in',
                   'study.iitm.ac.in', 'ds.study.iitm.ac.in']

# Define a list of blocked emails
blocked_emails = ['user@example.com']

# Define a list of admin emails
admin_emails = ['surajnish02@gmail.com',
                'studify.iitm@gmail.com', 'studify.dummy@gmail.com']


def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'profile' not in session:
            return redirect(url_for('login', next=request.url))

        user_info = session['profile']
        email = user_info['email']
        domain = email.split('@')[-1]

        if domain in allowed_domains or email in admin_emails:
            if email in blocked_emails:
                session.clear()
                return 'You are blocked. Contact admin for more details'
            else:
                session.permanent = True
                return func(*args, **kwargs)
        else:
            if re.match("/course/ns_2[3-9]{1}q[1-3]{1}_[a-z]{2}[0-9]{4}|/term/2[3-9]{1}q[1-3]", urlparse(request.url).path):
                session.permanent = True
                return func(*args, **kwargs)

            session.clear()
            return 'You are not authorized to access this page. Please use student email address.'

    return decorated_function
