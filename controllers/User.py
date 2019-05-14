from models import User
from flask import request, redirect, url_for
from schemas import UserSchema
from app import CORSify


def get_all_users():
    users = User.objects.all()
    return CORSify({"result": users})


def get_one_user(name):
    data = request.get_json()
    userID = data.get('id', "")
    user = User.objects.get(userID) \
        if 'id' in data and User.objects(pk=userID).count() \
        else None
    return CORSify({'result': user})


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
    return CORSify({'isValid': is_valid})


def del_user():
    data = request.get_json()
    is_valid = 'id' in data and User.objects(pk=data['id']).count() > 0
    if is_valid:
        user = User.objects.get(id=data['id'])
        if user:
            user.delete()
    return CORSify({'isValid': is_valid})


def del_all_users():
    print('hi')
    User.objects.delete()
    count = User.objects.count()
    return CORSify({'count': count})
