from gendiff.comparison.formatters.stylish import stylish
from gendiff.comparison.formatters.plain import plain
from gendiff.comparison.formatters.json import json_format


def get_format(tree, formatter):
    if formatter == 'stylish':
        return stylish(tree)
    elif formatter == 'plain':
        return plain(tree)
    elif formatter == 'json':
        return json_format(tree)