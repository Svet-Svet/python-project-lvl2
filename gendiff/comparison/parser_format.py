import json
import yaml
import os.path

from gendiff.comparison.comparison import generate_diff


def generate_parser_format(file1, file2, formatter):
    if os.path.splitext(file1[-4:]) == 'json':
        with open(file1, 'r') as file:
            file1 = json.load(file)
        with open(file2, 'r') as file:
            file2 = json.load(file)

        generate_diff(file1, file2, formatter)
    else:
        with open(file1, 'r') as file:
            file1 = yaml.safe_load(file)
        with open(file2, 'r') as file:
            file2 = yaml.safe_load(file)

        generate_diff(file1, file2, formatter)
