#!/usr/bin/env python3
"""basic flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """configuration class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)


@app.route('/')
def home() -> str:
    """renders a template 1-index.html"""
    return render_template('1-index.html')


def get_locale() -> str:
    """gets local language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.config.from_object(Config)
    babel = Babel(app, locale_selector=get_locale)
    app.run(debug=True)
