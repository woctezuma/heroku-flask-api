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


def get_suffixe(mirror_x=False, flip_y=False):
    suffixe = ""
    if mirror_x:
        suffixe += "x"
    if flip_y:
        suffixe += "y"
    if len(suffixe) > 0:
        suffixe = "." + suffixe
    return suffixe


def load_app_matches(mirror_x=False, flip_y=False):
    suffixe = get_suffixe(mirror_x=mirror_x, flip_y=flip_y)
    fname = get_data_folder() + "matches_faiss" + suffixe + get_npy_ext()
    return load_from_disk(fname)
