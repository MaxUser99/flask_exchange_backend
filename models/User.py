from app import db


class User(db.Document):
    email = db.StringField(max_length=60, required=True)
    name = db.StringField(max_length=60, required=True)
