from cerberus import Validator
v = Validator()


def validate(user):
    schema = {'name': {'type': 'string'}, 'email': {'type': 'string'}}
    return v.validate(user, schema)
