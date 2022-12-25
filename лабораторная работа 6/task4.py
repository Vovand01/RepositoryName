import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimeter=",") -> list[dict]:
    with open(filename) as f:
        headers = f.readline().rstrip().split(delimeter)
        dict_ = [dict(zip(headers, s.rstrip().split(delimeter))) for s in f.readlines()]
    return dict_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
