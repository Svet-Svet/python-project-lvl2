from gendiff.comparison.formatters.stylish import stylish
from gendiff.comparison.formatters.plain import plain


def get_format(tree, format):
    if format == 'stylish':
        return stylish(tree)
    elif format == 'plain':
        return plain(tree)
