from models import Task, User, Status, Category
# from models import Task
from flask import jsonify, request
from schemas import TaskSchema


def get_all_tasks():
    tasks = Task.objects.all()
    return jsonify({'result': tasks})


def get_get_one_tasks():
    data = request.get_json()
    task = Task.objects.get(id=data['id']) \
        if 'id' in data and Task.objects(pk=data['id']).count() \
        else None
    return jsonify({'result': task})


def add_task():
    data = request.get_json()
    is_valid = TaskSchema.is_valid_for_add(data)
    owner = None
    status = None
    category = None
    if is_valid:
        owner = User.objects.get(id=data['owner']) \
            if User.objects(pk=data['owner']) \
            else None
        status = Status.objects.get(id=data['status']) \
            if Status.objects(pk=data['status']) \
            else None
        category = Category.objects.get(id=data['category']) \
            if Category.objects(pk=data['category']) \
            else None
    is_valid &= status
    if is_valid:
        description = data['description'] if 'description' in data else ""
        new_task = Task(title=data['title'],
                        description=description,
                        # category=data['category'],
                        # owner=data['owner'],
                        status=data['status']
                        ).save()
        owner.update(push__posted_tasks=new_task.id)
        category.update(push__tasks=new_task.id)
    return jsonify({'isValid': is_valid})


def upd_task():
    pass
    # data = request.get_json()
    # is_valid = len(data.keys()) > 1 and TaskSchema.is_valid_for_update(data)
    # task = Task.objects.get(id=data['id']) \
    #     if is_valid and Task.objects(id=data['id']).count() \
    #     else None
    # if task:
    #     for key in data:
    #         allow = True
    #         if key == 'id':
    #             continue
    #         elif key == 'sub':
    #             curr_sub = User.objects.get(id=task[key]) if User.objects(id=task[key]).count() else None
    #             new_sub = User.objects.get(id=data[key]) if User.objects(id=data[key]).count() else None
    #             is_valid &= curr_sub and new_sub
    #             if is_valid:
    #                 curr_sub.update(pull__tasks=task.id)
    #                 new_sub.update(push__tasks=task.id)
    #         elif key == 'category':
    #             curr_cat = Category.objects.get(id=task[key]) if Category.objects(id=task[key]).count() else None
    #             new_cat = Category.objects.get(id=data[key]) if Category.objects(id=data[key]).count() else None
    #             is_valid &= curr_cat and new_cat
    #             if is_valid:
    #                 curr_cat.update(pull__tasks=task.id)
    #                 new_cat.update(push__tasks=task.id)
    #         elif key == 'status':
    #             new_stat = Status.objects.get(id=data[key]) if Status.objects(id=data[key]).count() else None
    #             is_valid &= new_stat
    #             allow = new_stat
    #
    #         if allow:
    #             task[key] = data[key]
    #
    #     if is_valid:
    #         task.save()
    #
    # return jsonify({"isValid": is_valid})


def del_task():
    data = request.get_json()
    is_valid = len(data.keys()) > 0 and TaskSchema.is_valid_for_delete(data)
    task = None
    if is_valid:
        title = data['title'] if 'title' in data else None
        _id = data['id'] if 'id' in data else None
        if title and Task.objects(title=title).count() > 0:
            task = Task.objects.get(title=title)
        elif _id and Task.objects(pk=_id).count() > 0:
            task = Task.objects.get(id=_id)

    if task:
        task.delete()

    return jsonify({'isValid': is_valid})


def del_all_tasks():
    Task.objects.delete()
    count = Task.objects.count()
    return jsonify({'count': count})

