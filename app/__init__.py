from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData
from configparser import ConfigParser


parser = ConfigParser()
parser.read("properties.ini")
params = parser.items("postgresql")

# dominio = f'postgresql://{params[3][1]}:{params[4][1]}@localhost:5432/{params[2][1]}'
# engine = create_engine(dominio)

engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres")

metadata = MetaData()
metadata.reflect(bind=engine, schema="draw_user")

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = dominio
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/postgres"
db = SQLAlchemy(app)

from app import models, routes

with app.app_context():
    if not list(metadata.tables.keys()):
        db.create_all()