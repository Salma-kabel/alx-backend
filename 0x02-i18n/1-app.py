#!/usr/bin/env python3
"""instantiate the Babel object in your app"""


from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

class Config:
    """ configure available languages in our app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

    app.config.from_object(Config)

@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """outputs “Welcome to Holberton” as page title"""
    return render_template('1-index.html')
