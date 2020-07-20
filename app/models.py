from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

from app.secretes import appkey

app.secret_key = appkey

class Dummymodel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name  =  db.Column(db.String(30), nullable = False)
    age = db.Column(db.Integer, nullable = True, default=None)
    def __repr__(self):
        return self.name