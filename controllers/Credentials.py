from models import Credentials, User
from flask import request
from schemas import CredentialsSchema
from app import CORSify


def contains_login(login):
    return Credentials.objects(login=login).count()


# for dev
def get_all():
    return CORSify({"result" : Credentials.objects.all()})


# create new credentials and user
def sign_in():
    data = request.get_json()
    login = data.get("login", "")
    is_valid = CredentialsSchema.is_valid_for_add(data) and not contains_login(login)
    credentials = None
    user = None
    if is_valid:
        user = User(rating=0, level=0, posted_tasks=[], subscribed_tasks=[]).save()
        credentials = Credentials(
            name=data['name'],
            login=data['login'],
            password=data['password'],
            user_id=user.id
        ).save()
        credentials.update(set__user_id=user.id)
    return CORSify({
        'user': user,
        'credentials': credentials,
        'isValid': is_valid
    })


# required login and password
def log_in():
    print("login method")
    data = request.get_json()
    print('data: ', data)
    is_valid = CredentialsSchema.is_valid_for_login(data)
    credentials = None
    print('is valid: ', is_valid)
    if is_valid and contains_login(data['login']):
        credentials = Credentials.objects.get(login=data['login'])
    return CORSify({
        'isValid': is_valid,
        'credentials': credentials
    })


# id <name, login, password>
def update_credentials():
    data = request.get_json()
    is_valid = CredentialsSchema.is_valid_for_update(data)
    credentials = Credentials.objects.get(id=data['id']) \
        if is_valid and Credentials.objects(id=data['id']).count() > 0 \
        else None
    if is_valid and credentials:
        for key in data:
            credentials[key] = data[key]
        credentials.save()
    return CORSify({'isValid': is_valid, 'credentials': credentials})


# id
def delete_credentials():
    data = request.get_json()
    _id = data.get('id', None)
    deleted = False
    if _id and Credentials.objects(id=_id).count() > 0:
        Credentials.objects.get(id=_id).delete()
        deleted = Credentials.objects(id=_id).count() == 0
    return CORSify({'deleted': deleted})


def delete_all_credentials():
    Credentials.objects.delete()
    count = Credentials.objects.count()
    return CORSify({'count': count})
