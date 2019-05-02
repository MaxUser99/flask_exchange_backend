from app import db


class Subcategory(db.Document):
    name = db.StringField(max_length=60, required=True, unique=True)
    parent_id = db.GenericReferenceField()
    subcategories = db.ListField(db.ReferenceField('self'))
    tasks = db.ListField(db.ReferenceField('task'))
