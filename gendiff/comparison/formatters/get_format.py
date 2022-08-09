from gendiff.comparison.formatters.comparison_yaml import generate_diff_yaml
from gendiff.comparison.formatters.comparison_json import generate_diff_json
from gendiff.comparison.formatters.stylish import stylish


def get_format(tree, format):
    if format == 'stylish':
        stylish(tree)