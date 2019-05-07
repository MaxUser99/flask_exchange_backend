from app import validator


def is_valid_for_update(data):
    schema = {
        'id': {'type': 'string', 'required': True},
        'rating': {'type': 'number'},
        'level': {'type': 'number'},
    }
    return validator.validate(data, schema)
