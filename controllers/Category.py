from models import Category
from flask import jsonify, request
from schemas import CategorySchema


def get_all_categories():
    categories = Category.objects.all()
    return jsonify({"result": categories})


def get_one_category(name):
    subcat = Category.objects.get(name=name) if Category.objects(name=name).count() else None
    return jsonify({'result': subcat})


def add_category():
    data = request.get_json()
    parent = None
    is_valid = CategorySchema.is_valid_for_add(data)
    if 'parent_id' in data:
        parent = Category.objects.get(id=data['parent_id'])\
            if Category.objects(pk=data['parent_id']).count()\
            else None

    if is_valid and Category.objects(name=data['name']).count() == 0:
        new_category = Category(name=data['name'], parent_id=parent.id)\
            if parent\
            else Category(name=data['name'])

        new_category.save()

        if parent:
            parent.update(push__subcategories=new_category.id)

    return jsonify({"isValid": is_valid}), 200 if is_valid else 400


def upd_category():
    data = request.get_json()
    is_valid = len(data.keys()) > 1 and CategorySchema.is_valid_for_update(data)
    category = Category.objects.get(id=data['id']) \
        if is_valid and Category.objects(id=data['id']).count() \
        else None

    if category:
        for key in data:
            if key == 'id':
                continue
            category[key] = data[key]
        category.save()

    return jsonify({'isValid': is_valid})


def del_category():
    data = request.get_json()
    is_valid = len(data.keys()) > 0 and CategorySchema.is_valid_for_delete(data)
    category = None
    if is_valid:
        name = data['name'] if 'name' in data else None
        _id = data['id'] if 'id' in data else None
        if name and Category.objects(name=name).count() > 0:
            category = Category.objects.get(name=name)
        elif _id and Category.objects(pk=_id).count() > 0:
            category = Category.objects.get(id=_id)

    if category:
        category.delete()

    return jsonify({'isValid': is_valid})


def del_all_categories():
    Category.objects.delete()
    count = Category.objects.count()
    return jsonify({'count': count})

