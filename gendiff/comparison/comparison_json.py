import json
from gendiff.comparison.comparison import generate_diff


def generate_diff_json(file1, file2):
    with open(file1, 'r') as file:
        file1 = json.load(file)
    with open(file2, 'r') as file:
        file2 = json.load(file)

    merged_dict = file1 | file2

    generate_diff(merged_dict, file1, file2)
