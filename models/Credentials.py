from app import db


class Credentials(db.Document):
    user_id = db.ReferenceField('User', reverse_delete_rule=db.CASCADE)
    name = db.StringField(max_length=60, required=True)
    login = db.StringField(max_length=20, required=True)
    password = db.StringField(max_length=20, required=True)

