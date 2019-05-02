from models import Category
from flask import jsonify, request
from schemas import CategorySchema


def get_category_by_name(name):
    category = Category.objects.get(name=name)
    return jsonify({'result': category})


def get_category_by_id(id):
    category = Category.objects.get(id=id)
    return jsonify({'result': category})


def update_category():
    data = request.get_json()
    is_valid = len(data.keys()) > 0 and CategorySchema.is_valid_for_update(data)
    if is_valid:
        category = Category.objects.get(id=data['id'])
        if category:
            category.update(
                set__name=data['name'],
                set__subcategories=data['subcategories']
            )
    return jsonify({'isValid': is_valid})


def del_category():
    data = request.get_json()
    is_valid = len(data.keys()) > 0 and CategorySchema.is_valid_for_delete(data)
    if is_valid:
        name = data['name'] if 'name' in data else None
        cat_id = data['id'] if 'id' in data else None
        if cat_id:
            Category.objects.get(id=id).delete()
        elif name:
            Category.objects(name=name).delete()
    return jsonify({'isValid': is_valid})


def get_all_categories():
    categories = Category.objects.all()
    return jsonify({"result": categories})


def add_category():
    data = request.get_json()
    is_valid = CategorySchema.is_valid_for_add(data)
    if is_valid and Category.objects(name=data["name"]).count() == 0:
        Category(name=data["name"]).save()
    return jsonify({"isValid": is_valid}), 200 if is_valid else 400


def clear_all_categories():
    Category.objects.delete()
    count = Category.objects.count()
    return jsonify({'count': count})
