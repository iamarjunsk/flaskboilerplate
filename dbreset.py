from app.models import db

db.drop_all()
db.create_all()
print('db reseted')