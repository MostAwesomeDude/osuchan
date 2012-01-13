from flask import Flask

from osuchan.blueprint import osuchan

app = Flask(__name__)

app.register_blueprint(osuchan)

app.debug = True
