from flask import Flask
from utils import *

app = Flask(__name__)

from Apps.main import main
from Apps.crop import crop
from Apps.error import error
from Api.Api import api

app.register_blueprint(main)
app.register_blueprint(crop)
app.register_blueprint(error)

api.init_app(app)
