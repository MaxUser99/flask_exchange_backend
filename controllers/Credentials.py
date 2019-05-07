from models import Credentials, User
from flask import jsonify, request
from schemas import CredentialsSchema


def contains_login(login):
    return Credentials.objects(login=login).count()


# create new credentials and user
def sign_in():
    data = request.get_json()
    login = data['login'] if 'login' in data else ""
    is_valid = CredentialsSchema.is_valid_for_add(data) and not contains_login(login)
    credentials = None
    user = None
    if is_valid:
        credentials = Credentials(name=data['name'], login=data['login'], password=data['password']).save()
        user = User(rating=0, level=0, posted_tasks=[], subscribed_tasks=[], credentials=credentials.id).save()
        credentials.update(set_user_id=user.id)
    return jsonify({'user': user, 'credentials': credentials})


# required login and password
def log_in():
    data = request.get_json()
    is_valid = CredentialsSchema.is_valid_for_login(data)
    user = None
    credentials = None
    if is_valid and contains_login(data['login']):
        credentials = Credentials.objects.get(login=data['login'])
        user = User.credentials.get(id=credentials.user_id)
    return jsonify({
        'isValid': is_valid,
        'user': user,
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
    return jsonify({'isValid': is_valid, 'credentials': credentials})


# id
def delete_credentials():
    data = request.get_json()
    _id = data['id'] if 'id' in data else None
    deleted = False
    if _id and Credentials.objects(id=_id).count() > 0:
        Credentials.objects.get(id=_id).delete()
        deleted = Credentials.objects(id=_id).count() == 0
    return jsonify({'deleted': deleted})


def delete_all_credentials():
    Credentials.objects.delete()
    count = Credentials.objects.count()
    return jsonify({'count': count})
