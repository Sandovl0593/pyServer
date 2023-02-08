from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData
import os, os.path

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')

metadata = MetaData()
metadata.reflect(bind=engine, schema="draw_user")

# def del_pycache(path):
#     if os.path.isdir(path):
#         if "__pycache__" in path:
#             os.unlink(path)
#         else:
#             for filename in os.listdir(path):
#                 del_pycache(f"{path}/{filename}")

# del_pycache("../pyServer")

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/postgres"
db = SQLAlchemy(app)

from app import models, routes

with app.app_context():
    if not list(metadata.tables.keys()):
        db.create_all()