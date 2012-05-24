from flask import Flask
from flaskext.mail import Mail
import os

CURRENT_DIR = os.path.realpath(os.path.dirname(__file__))
app = Flask(__name__)
app.config.from_pyfile(os.path.join(CURRENT_DIR, 'config.py'))
mail = Mail(app)

import barcodes.views

if __name__ == '__main__':
    if app.debug:
        app.run(host='0.0.0.0')
    else:
        app.run()
