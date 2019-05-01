from models import Category
from flask import jsonify, request
from schemas import CategorySchema


def get_all_categories():
    categories = Category.objects.all()
    return jsonify({"result": categories})


def add_category():
    data = request.get_json()
    is_valid = CategorySchema.is_valid(data)
    print("is_valid: ", is_valid)
    if is_valid:
        Category(name=data["name"]).save()
    return jsonify({"isValid": is_valid}), 200 if is_valid else 400


def clear_all_categories():
    Category.objects.delete()
    count = Category.objects.count()
    return jsonify({'count': count})

