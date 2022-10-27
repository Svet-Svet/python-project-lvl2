import json
import yaml


def generate_parser_format(file):
    if file.endswith('.json'):
        with open(file, 'r') as file:
            return json.load(file)
    elif file.endswith('.yml') or file.endswith('.yaml'):
        with open(file, 'r') as file:
            return yaml.safe_load(file)
    raise Exception('Invalid file format.')
