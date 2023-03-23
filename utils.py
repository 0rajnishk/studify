from functools import wraps
from flask import session, redirect, url_for, request
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
