from cerberus import Validator
v = Validator()


def is_valid(user):
    schema = {'name': {'type': 'string'}, 'email': {'type': 'string'}}
    return v.validate(user, schema)
