from models import User
from flask import jsonify, request
from schemas import UserSchema


def all_users():
    users = User.objects.all()
    return jsonify({"result": users})


def add_user():
    data = request.get_json()
    print(data)
    return jsonify({
        "json_data": data,
        "isValid": UserSchema.validate(data)
    })
