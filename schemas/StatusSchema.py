from app import validator


def is_valid_for_upd(status):
    schema = {
        'id': {'type': 'string', 'required': True},
        'name': {'type': 'string', 'required': True}
    }
    return validator.validate(status, schema)
