from models import User
from flask import jsonify, request, redirect, url_for
from schemas import UserSchema


def all_users():
    users = User.objects.all()
    return jsonify({"result": users})


def add_user():
    user_data = request.get_json()
    print(user_data)
    print(user_data["email"])
    is_valid = UserSchema.is_valid(user_data)
    if is_valid:
        user = User(name=user_data["name"], email=user_data["email"])
        user.save()
    return jsonify({"isValid": is_valid}), 200 if is_valid else 400


def clear():
    User.objects.delete()
    return redirect(url_for("all_users"))
