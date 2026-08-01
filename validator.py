import json
def check(data_str):
    try:
        json.loads(data_str)
        return True
    except ValueError:
        return False