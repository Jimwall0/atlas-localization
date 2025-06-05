from flask import Flask, request
from flask_babel import Babel, _

app = Flask(__name__)

# Configure available languages
app.config['BABEL_DEFAULT_LOCALE'] = 'fr'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'


babel = Babel(app)


def get_locale():
    # Use request headers or a user-specific preference to determine locale
    return request.accept_languages.best_match(['en', 'fr'])


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index():
    # This will display the string in the appropriate language
    gretting = _("Hello, World!")
    return gretting


if __name__ == "__main__":
    app.run()
