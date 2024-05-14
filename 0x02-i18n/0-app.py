#!/usr/bin/env python3
"""setup a basic Flask app"""


from flask import Flask, render_template


app = Flask(__name__)
@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """outputs “Welcome to Holberton” as page title"""
    return render_template('0-index.html')
