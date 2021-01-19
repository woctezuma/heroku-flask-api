from utils.file_utils import load_app_ids, load_app_names, load_app_matches
from utils.url_utils import (
    get_steam_store_url,
    get_steamdb_url,
    get_query_url,
    get_steam_illustration_url,
)


def index_to_id(index):
    app_ids = load_app_ids()
    return app_ids[int(index)]


def index_to_name(index):
    app_names = load_app_names()
    return app_names[int(index)]


def index_to_app(index):
    id = index_to_id(index)

    return {
        "index": int(index),
        "id": id,
        "name": index_to_name(index),
        "steam_store_url": get_steam_store_url(id),
        "steam_illustration_url": get_steam_illustration_url(id),
        "steamdb_url": get_steamdb_url(id),
        "query_url": get_query_url(id),
    }


def index_to_matches(index, num_matches=-1):
    app_matches = load_app_matches()
    matches = app_matches[int(index), :]
    max_length = int(num_matches)
    if max_length >= 0:
        matches = matches[:max_length]
    return [int(i) for i in matches]


def index_to_similar_apps(index, num_matches=-1):
    indices = index_to_matches(index)
    max_length = max(-1, int(num_matches))

    app_list = []
    for count, i in enumerate(indices):
        if count == max_length:
            break
        app_list.append(index_to_app(i))
    return app_list
