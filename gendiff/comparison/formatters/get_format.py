from gendiff.comparison.formatters.stylish import stylish
from gendiff.comparison.formatters.plain import plain


def get_format(tree, formatter):
    if formatter == 'stylish':
        return stylish(tree)
    elif formatter == 'plain':
        return plain(tree)
