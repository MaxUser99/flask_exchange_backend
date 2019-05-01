from flask import jsonify
from models import User
from app import app


@app.route('/')
def index():
    count = User.objects.count()
    return jsonify({"cont": count})
