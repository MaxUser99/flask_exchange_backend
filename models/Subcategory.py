from app import db


# TODO add tasks list
class Subcategory(db.Document):
    category_id = db.ReferenceField('Category')
    subcategories = db.ListField(db.ReferenceField('self'))
