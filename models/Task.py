from app import db


class Task(db.Document):
    title = db.StringField(max_length=60, required=True)
    description = db.StringField(required=True)
    category = db.ReferenceField('Category', reverse_delete_rule=db.NULLIFY)
    # owner
    # sub
    status = db.ReferenceField('Status')
