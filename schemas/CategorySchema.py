from app import validator


def validate(item, schema):
    res = validator.validate(item, schema)
    if res is False:
        print(validator.errors)
    return res


def is_valid_for_delete(category):
    schema = {
        'name': {
            'type': 'string'
        },
        'id': {
            'type': 'string'
        }
    }
    return validate(category, schema)


def is_valid_for_add(category):
    schema = {
        'name': {'type': 'string', 'required': True},
        'description': {'type': 'string', 'required': True}
    }
    return validate(category, schema)
