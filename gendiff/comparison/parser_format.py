import json
import yaml
import os.path


def generate_parser_format(file):
    if os.path.splitext(file[-4:]) == 'json':
        with open(file, 'r') as file:
            file = json.load(file)
            return file
    else:
        with open(file, 'r') as file:
            file = yaml.safe_load(file)
            return file
