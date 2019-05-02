from app import db


class Status(db.Document):
    name = db.StringField(max_length=60, required=True, unique=True)

