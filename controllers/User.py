from models import User
from flask import jsonify, request, redirect, url_for
from schemas import UserSchema


def all_users():
    users = User.objects.all()
    return jsonify({"result": users})


def add_user():
    user_data = request.get_json()
    is_valid = UserSchema.is_valid(user_data)
    print("is_valid: ", is_valid)
    if is_valid:
        User(name=user_data["name"], email=user_data["email"]).save()
    return jsonify({"isValid": is_valid}), 200 if is_valid else 400


def clear():
    User.objects.delete()
    return redirect(url_for("all_users"))
