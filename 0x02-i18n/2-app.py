#!/usr/bin/env python3
"""Create a get_locale function with the
babel.localeselector decorator"""


from flask import Flask, render_template, request
from flask_babel import Babel, negotiate_locale


class Config:
    """ configure available languages in our app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """outputs “Welcome to Holberton” as page title"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
