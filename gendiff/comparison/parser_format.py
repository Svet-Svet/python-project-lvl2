import json
import yaml


def generate_parser_format(file_path):
    with open(file_path, 'r') as _f:
        if file_path.endswith('.json'):
            return json.load(_f)
        elif file_path.endswith('.yml') or file_path.endswith('.yaml'):
            return yaml.safe_load(_f)
        raise Exception('Invalid file format.')
