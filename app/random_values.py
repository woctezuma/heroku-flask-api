import random

from utils.file_utils import load_app_ids, load_app_names


def get_random_index():
    app_ids = load_app_ids()
    return random.randrange(len(app_ids))


def get_random_id():
    app_ids = load_app_ids()
    return random.choice(app_ids)


def get_random_name():
    app_names = load_app_names()
    return random.choice(app_names)
