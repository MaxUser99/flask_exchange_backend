from app import db


class Category(db.Document):
    name = db.StringField(max_length=60, required=True, unique=True)
    parent_id = db.ReferenceField('self', reverse_delete_rule=db.CASCADE)
    subcategories = db.ListField(db.ReferenceField('self', reverse_delete_rule=db.PULL))
    # tasks = db.ListField(db.ReferenceField('Task'))
    tasks = db.ListField(db.ReferenceField('Task', reverse_delete_rule=db.PULL))
