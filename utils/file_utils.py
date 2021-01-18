from utils.disk_utils import get_json_ext, get_npy_ext, load_from_disk


def get_data_folder():
    return "data/"


def load_app_ids(from_json=False):
    if from_json:
        file_ext = get_json_ext()
    else:
        file_ext = get_npy_ext()
    fname = get_data_folder() + "app_ids" + file_ext
    return [int(app_id) for app_id in load_from_disk(fname)]


def load_app_names():
    fname = get_data_folder() + "app_names" + get_json_ext()
    return load_from_disk(fname)


def load_app_matches():
    fname = get_data_folder() + "matches" + get_npy_ext()
    return load_from_disk(fname)
