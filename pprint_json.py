import json
from os import path
from sys import argv
from pprint import PrettyPrinter


def load_data(filepath):
    if not path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def pretty_print_json(data):
    pp = PrettyPrinter(indent=4, width=120, depth=None, compact=True)
    return pp.pprint(data)


if __name__ == '__main__':
    if len(argv) is 1 or len(argv) >= 3:
        print('\nPlease, specify the file for opening. Example: python pprint_json.py alcomarket.json\n')
    else:
        outer_json_file = load_data(argv[1])
        print(pretty_print_json(outer_json_file))
