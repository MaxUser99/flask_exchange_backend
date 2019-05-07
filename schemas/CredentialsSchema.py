from app import validator


def is_valid_for_add(credentials):
    schema = {
        'name': {'type': 'string', 'required': True},
        'login': {'type': 'string', 'required': True},
        'password': {'type': 'string', 'required': True},
    }
    return validator.validate(credentials, schema)


def is_valid_for_login(credentials):
    schema = {
        'login': {'type': 'string', 'required': True},
        'password': {'type': 'string', 'required': True},
    }
    return validator.validate(credentials, schema)


def is_valid_for_update(credentials):
    schema = {
        'id': {'type': 'string', 'required': True},
        'name': {'type': 'string'},
        'login': {'type': 'string'},
        'password': {'type': 'string'},
    }
    return validator.validate(credentials, schema)
