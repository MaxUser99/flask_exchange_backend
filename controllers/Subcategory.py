from models import Subcategory, Category
from flask import jsonify, request
from schemas import SubcategorySchema


def get_all_subcat():
    categories = Subcategory.objects.all()
    return jsonify({"result": categories})


def get_one_subcat(name):
    subcat = Subcategory.objects.get(name=name)
    return jsonify({'result': subcat})


def add_subcat():
    data = request.get_json()
    parent = None
    is_valid = SubcategorySchema.is_valid_for_add(data)
    if is_valid:
        parent_id = data['parent_id']
        if Subcategory.objects(pk=parent_id).count():
            parent = Subcategory.objects.get(id=parent_id)
        elif Category.objects(pk=parent_id).count():
            parent = Category.objects.get(id=parent_id)
    if parent:
        subcat = Subcategory(name=data["name"], parent_id=parent.id)
        subcat.save()
        parent.update(push__subcategories=subcat.id)
    return jsonify({"isValid": is_valid}), 200 if is_valid else 400


def upd_subcat():
    data = request.get_json()
    is_valid = len(data.keys()) > 0 and SubcategorySchema.is_valid_for_update(data)
    if is_valid:
        subcat = Subcategory.objects.get(id=data['id']) if Subcategory.objects(id=data['id']).count() else None
        if subcat:
            subcat.update(
                set__name=data['name'],
                set__subcategories=data['subcategories'],
                set__tasks=data['tasks'],
            )
    return jsonify({'isValid': is_valid})


def del_subcat():
    data = request.get_json()
    is_valid = len(data.keys()) > 0 and SubcategorySchema.is_valid_for_delete(data)
    if is_valid:
        name = data['name'] if 'name' in data else None
        _id = data['id'] if 'id' in data else None
        parent = None
        subcat = None
        if _id:
            subcat = Subcategory.objects.get(id=id)
        elif name:
            subcat = Subcategory.objects.get(name=name)

        if subcat:
            if Subcategory.objects(subcategories__in=subcat.id).count():
                parent = Subcategory.objects.get(subcategories__in=subcat.id)
            elif Category.objects(subcategories__in=subcat.id).count():
                parent = Category.objects.get(subcategories__in=subcat.id)

        if parent:
            parent.subcategories.remove(subcat.id)
            parent.save()
            subcat.delete()

    return jsonify({'isValid': is_valid})


def del_all_subcat():
    Subcategory.objects.delete()
    count = Subcategory.objects.count()
    return jsonify({'count': count})

