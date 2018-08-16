from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from app import app


db = SQLAlchemy(app)
ma = Marshmallow(app)
Migrate(app, db)