from flask import jsonify
from models import User
from app import app, CORSify


@app.route('/')
def index():
    count = User.objects.count()
    return CORSify(jsonify({"cont": count}))

