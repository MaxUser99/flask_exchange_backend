from cerberus import Validator
v = Validator()


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
    return v.validate(user, schema)
