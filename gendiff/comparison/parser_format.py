import json
import yaml


def generate_parser_format(file):
    if file.endswith('.json'):
        with open(file, 'r') as file:
            file = json.load(file)
            return file
    elif file.endswith('.yml') or file.endswith('.yaml'):
        with open(file, 'r') as file:
            file = yaml.safe_load(file)
            return file
    raise Exception('Invalid file format.')
