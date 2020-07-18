from app import app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/yt'
from app.secretes import appkey

app.secret_key = appkey

class Dummymodel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name  =  db.Column(db.String(30), nullable = False)
