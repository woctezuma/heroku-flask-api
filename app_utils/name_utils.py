from app_utils.index_utils import (
    index_to_id,
    index_to_app,
    index_to_similar_apps,
)
from utils.file_utils import load_app_names


def name_to_index(name):
    app_names = load_app_names()
    return app_names.index(name)


def name_to_id(name):
    index = name_to_index(name)
    return index_to_id(index)


def name_to_app(name):
    index = name_to_index(name)
    return index_to_app(index)


def name_to_similar_apps(name, num_matches=-1):
    index = name_to_index(name)
    return index_to_similar_apps(index, num_matches)
