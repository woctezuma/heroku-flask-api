from app_utils.index_utils import (
    index_to_name,
    index_to_app,
    index_to_similar_apps,
)
from utils.file_utils import load_app_ids


def id_to_index(id):
    app_ids = load_app_ids()
    return app_ids.index(int(id))


def id_to_name(id):
    index = id_to_index(id)
    return index_to_name(index)


def id_to_app(id):
    index = id_to_index(id)
    return index_to_app(index)


def id_to_similar_apps(id, num_matches=10):
    index = id_to_index(id)
    return index_to_similar_apps(index, num_matches)
