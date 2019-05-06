from app import validator


def is_valid_for_add(data):
    schema = {
        'title': {'type': 'string', 'required': True},
        'description': {'type': 'string'},
        'category': {'type': 'string', 'required': True},
        'owner': {'type': 'string', 'required': True},
        'status': {'type': 'string', 'required': True},
    }
    return validator.validate(data, schema)


def is_valid_for_update(data):
    schema = {
        'title': {'type': 'string', 'required': True},
        'description': {'type': 'string'},
        'category': {'type': 'string', 'required': True},
        'sub': {'type': 'string'},
        'status': {'type': 'string', 'required': True},
    }
    return validator.validate(data, schema)


def is_valid_for_delete(category):
    schema = {
        'title': {'type': 'string'},
        'id': {'type': 'string'}
    }
    return validator.validate(category, schema)
