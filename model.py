import json


def save_model(Q, path):
    with open(path, "w") as f:
        json.dump(Q, f)


def load_model(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
