from gendiff.comparison.formatters.stylish import stylish
from gendiff.comparison.formatters.plain import plain
from gendiff.comparison.formatters.json import json_format


FORMATTERS = {
    'stylish': stylish,
    'plain': plain,
    'json': json_format
}


def get_formatted_output(tree, format_output='stylish'):
    formatter = FORMATTERS[format_output]
    return formatter(tree)
