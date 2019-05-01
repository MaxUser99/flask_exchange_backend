from app import db


class Category(db.Document):
    name = db.StringField(max_length=60, required=True, unique=True)
    subcutegories = db.ListField(db.ReferenceField('Subcategory'))
