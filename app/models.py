from app import db
from sqlalchemy import Integer, String, TIMESTAMP
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'draw_user'}

    id = db.Column(Integer(), primary_key=True, autoincrement=True)
    username = db.Column(String(255), index=True, unique=True)
    country = db.Column(String(255), index=True)
    color = db.Column(String(255), index=True)
    date_at = db.Column(TIMESTAMP, index=True, unique=True)

    # password = db.Column(String(255))
    def __init__(self, username, country, color):
        self.username = username
        self.country = country
        self.color = color
        self.date_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #permite imprimir el objeto usuario y mostrar datos
    def __repr__(self):
        return '<User %r>' % self.username
    