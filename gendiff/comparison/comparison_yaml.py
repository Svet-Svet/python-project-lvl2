import yaml
from gendiff.comparison.comparison import generate_diff


def generate_diff_yaml(file1, file2):
    with open(file1, 'r') as file:
        file1 = yaml.safe_load(file)
    with open(file2, 'r') as file:
        file2 = yaml.safe_load(file)

    merged_dict = file1 | file2

    generate_diff(merged_dict, file1, file2)
