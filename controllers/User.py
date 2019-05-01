from models import User
from flask import jsonify, request
from schemas import UserSchema


def all_users():
    users = User.objects.all()
    return jsonify({"result": users})


def add_user():
    user_data = request.get_json()
    print(user_data)
    is_valid = UserSchema.is_valid(user_data)
    return jsonify({"isValid": is_valid}), 200 if is_valid else 400
