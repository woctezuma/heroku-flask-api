import json

import numpy as np


def get_json_ext():
    return '.json'


def get_npy_ext():
    return '.npy'


def load_json(fname):
    with open(fname, 'r') as f:
        data = json.load(f)
    return data


def load_npy(fname):
    return np.load(fname)


def load_from_disk(fname):
    if fname.endswith(get_json_ext()):
        data = load_json(fname)
    elif fname.endswith(get_npy_ext()):
        data = load_npy(fname)
    else:
        data = None
    return data
