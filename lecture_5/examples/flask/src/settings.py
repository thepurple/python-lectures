from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


APP_HOST = "0.0.0.0"

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'\
    .format(os.path.join(basedir, 'flask_db.sqlite'))
db = SQLAlchemy(app)
ma = Marshmallow(app)
