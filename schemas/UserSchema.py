from app import validator


def is_valid(user):
    schema = {
        'name': {
            'required': True,
            'type': 'string'
        },
        'email': {
            'required': True,
            'type': 'string'
        }
    }
    return validator.validate(user, schema)
