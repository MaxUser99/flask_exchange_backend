from app import db


class User(db.Document):
    rating = db.FloatField(min_value=0, max_value=100)
    level = db.FloatField(min_value=0, max_value=100)
    posted_tasks = db.ListField(db.ReferenceField('Task', reverse_delete_rule=db.PULL))
    subscribed_tasks = db.ListField(db.ReferenceField('Task', reverse_delete_rule=db.PULL))
    credentials = db.ReferenceField("Credentials", reverse_delete_rule=db.CASCADE)
