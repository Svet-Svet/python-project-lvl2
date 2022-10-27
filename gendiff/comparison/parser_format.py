import json
import yaml


def generate_parser_format(file):
    with open(file, 'r') as file:
        if file.endswith('.json'):
            file_path = json.load(file)
            return file_path
        elif file.endswith('.yml') or file.endswith('.yaml'):
            file_path = yaml.safe_load(file)
            return file_path
        raise Exception('Invalid file format.')
