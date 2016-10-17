from flask import render_template
from google.appengine.api import users

from application import app

def home():
    user = users.get_current_user()
    email = user.email()
    return render_template('base.html', email=email)


def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

    """
    return ''