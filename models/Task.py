from app import db


class Task(db.Document):
    title = db.StringField(max_length=60, required=True)
    description = db.StringField(required=True)
    status = db.ReferenceField('Status')
