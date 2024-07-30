#!/usr/bin/env python3
"""basic flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel
from flask_babel import gettext as _
from typing import Dict

class Config:
    """configuration class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    DEBUG = True


def get_locale() -> str:
    """gets local language"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app, locale_selector=get_locale)


@app.context_processor
def inject_translations() -> Dict:
    return dict(_=_)


@app.route('/')
def home() -> str:
    """renders a template 1-index.html"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True, port=3000)
