from models import User
from flask import jsonify, request, redirect, url_for
from schemas import UserSchema


def get_all_users():
    users = User.objects.all()
    return jsonify({"result": users})


def get_one_user(name):
    data = request.get_json()
    user = User.objects.get(id=data['id']) \
        if 'id' in data and User.objects(pk=data['id']).count() \
        else None
    return jsonify({'result': user})


# user will be created when new credentials are created
# def add_user():


def upd_user():
    data = request.get_json()
    is_valid = len(data.keys()) > 0 and UserSchema.is_valid_for_update(data)
    user = User.objects.get(id=data['id']) \
        if 'id' in data and User.objects(pk=data['id']).count() \
        else None
    if is_valid and user:
        for key in data:
            if key == 'id':
                continue
            user[key] = data[key]
        user.save()
    return jsonify({'isValid': is_valid})


def del_user():
    data = request.get_json()
    is_valid = len(data.keys()) > 0 \
               and 'id' in data \
               and User.objects(pk=data['id']).count() > 0
    if is_valid:
        user = User.objects.get(id=data['id'])
        if user:
            user.delete()
    return jsonify({'isValid': is_valid})


def del_all_users():
    User.objects.delete()
    count = User.objects.count()
    return jsonify({'count': count})
