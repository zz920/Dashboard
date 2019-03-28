import os
from ast import literal_eval

import environ

env = environ.Env()
CURRENT_DIR = os.path.dirname(__file__)
environ.Env.read_env(os.path.join(CURRENT_DIR, '.env'))  # reading .env file


def getenv(key, default=None, **kwargs):
    """
    Retrieve environment variable by key and casts the value to desired type.
    If desired type is list or tuple - uses separator to split the value.
    """
    desired_type = kwargs.pop('type', str)
    list_separator = kwargs.pop('sep', ',')

    value = os.getenv(key, None)

    if value is None:
        return default

    if desired_type is int:
        return desired_type(value)

    if desired_type is bool:
        return False if value.lower() in ['false', '0'] else True

    if desired_type in [list, tuple]:
        value = value.split(list_separator)
        return desired_type(value)

    if desired_type is dict:
        return dict(literal_eval(value))

    return desired_type(value)
