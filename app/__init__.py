from flask import Flask, Blueprint
from flask_cors import CORS
from app.api import api
import os


basedir = os.path.dirname(os.path.abspath(__file__))
db_file = 'sqlite:///' + os.path.join(basedir, './db/user.db')

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = db_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app import models
from app.api.user_service import ns as user_api

blueprint = Blueprint('api', __name__, url_prefix='/service')
api.init_app(blueprint)

api.add_namespace(user_api)

app.register_blueprint(blueprint)