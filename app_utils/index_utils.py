from utils.file_utils import load_app_ids, load_app_names, load_app_matches


def index_to_id(index):
    app_ids = load_app_ids()
    return app_ids[int(index)]


def index_to_name(index):
    app_names = load_app_names()
    return app_names[int(index)]


def index_to_app(index):
    return {"index": int(index), "id": index_to_id(index), "name": index_to_name(index)}


def index_to_matches(index, num_matches=-1):
    app_matches = load_app_matches()
    max_length = max(-1, int(num_matches))
    matches = app_matches[int(index), :max_length]
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
