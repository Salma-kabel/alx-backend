#!/usr/bin/env python3
"""instantiate the Babel object in your app"""


from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ configure available languages in our app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """outputs “Welcome to Holberton” as page title"""
    return render_template('1-index.html')
