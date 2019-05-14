from models import Status
from flask import request
from schemas import StatusSchema
from app import CORSify


def get_all_statuses():
    statuses = Status.objects.all()
    return CORSify({'result': statuses})


def get_one_status(name):
    status = Status.objects.get(name=name) if Status.objects(name=name).count() else None
    return CORSify({'result': status})


def add_status():
    data = request.get_json()
    is_valid = 'name' in data
    if is_valid:
        Status(name=data['name']).save()
    return CORSify({"isValid": is_valid}), 200 if is_valid else 400


def upd_status():
    data = request.get_json()
    is_valid = StatusSchema.is_valid_for_upd(data)
    if is_valid and Status.objects(pk=data['id']).count() > 0:
        Status.objects(pk=data['id']).update_one(set__name=data['name'])
    return CORSify({'isValid': is_valid})


def del_status():
    data = request.get_json()
    is_valid = len(data.keys()) > 0 and StatusSchema.is_valid_for_delete(data)
    status = None
    if is_valid:
        name = data['name'] if 'name' in data else None
        _id = data['id'] if 'id' in data else None
        if name and Status.objects(name=name).count() > 0:
            status = Status.objects.get(name=name)
        elif _id and Status.objects(pk=_id).count() > 0:
            status = Status.objects.get(id=_id)

    if status:
        status.delete()

    return CORSify({'isValid': is_valid})


def del_all_statuses():
    Status.objects.delete()
    count = Status.objects.count()
    return CORSify({'count': count})



