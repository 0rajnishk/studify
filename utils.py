from functools import wraps
from flask import session, redirect, url_for, request
import re
from urllib.parse import urlparse

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
            if not (re.match("^/course/ns_[0-9]{2}q[1-4]?[0-9]_[a-z]{2}[0-9]{4}$", urlparse(request.url).path) or
                    re.match("^/term/([2-3][3-9]q[1-3]|23q1)$", urlparse(request.url).path)):
                return redirect(url_for('login', next=request.url))
            else:
                session.permanent = True
                return func(*args, **kwargs)

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
            session.clear()
            return 'You are not authorized to access this page. Please use student email address.'

    return decorated_function
