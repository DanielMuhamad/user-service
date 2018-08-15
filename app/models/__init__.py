from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app


db = SQLAlchemy(app)
Migrate(app, db)


from app.models.users import User