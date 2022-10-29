from gendiff.comparison.formatters.stylish import stylish
from gendiff.comparison.formatters.plain import plain
from gendiff.comparison.formatters.json import json_format


FORMATTERS = {
    'stylish': stylish,
    'plain': plain,
    'json': json_format
}


def get_format(tree, formats='stylish'):
    formatter = FORMATTERS[formats]
    return formatter(tree)
