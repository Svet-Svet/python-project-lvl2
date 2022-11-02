ADDED = 'added'
REMOVED = 'removed'
IDENTICAL = 'identical'
CHANGED = 'changed'


# flake8: noqa: max-complexity: 10
def stylish(graph, _deep=0):
    replacer = ' '
    result = ''
    parenthesis_start = "{"
    parenthesis_end = "}"
    count_spaces = replacer * (_deep + 2)
    quote_spaces = replacer * _deep
    for node in graph:
        status, key, *values = node
        value = is_bool(node[2])
        if isinstance(node[2], list):
            if status == ADDED:
                keys = f'\n{count_spaces}+ {node[1]}: '
                result += keys + stylish(node[2], _deep + 4)
            elif status == REMOVED:
                keys = f'\n{count_spaces}- {node[1]}: '
                result += keys + stylish(node[2], _deep + 4)
            elif status == IDENTICAL:
                keys = f'\n{count_spaces}  {node[1]}: '
                result += keys + stylish(node[2], _deep + 4)
            elif status == CHANGED:
                old = f'\n{count_spaces}- {node[1]}: '
                new = f'\n{count_spaces}+ {node[1]}: {is_bool(node[3])}'
                result += old + stylish(node[2], _deep + 4)
                result += new
        elif status == CHANGED and isinstance(node[3], list):
                old = f'\n{count_spaces}- {node[1]}: {value}'
                new = f'\n{count_spaces}+ {node[1]}: '\
                      + stylish(node[3], _deep + 4)
                result += old
                result += new
        elif status == ADDED:
            result += f'\n{count_spaces}+ {node[1]}: {value}'
        elif status == REMOVED:
            result += f'\n{count_spaces}- {node[1]}: {value}'
        elif status == IDENTICAL:
            result += f'\n{count_spaces}  {node[1]}: {value}'
        elif status == CHANGED:
            result += f'\n{count_spaces}- {node[1]}: {value}'
            result += f'\n{count_spaces}+ {node[1]}: {is_bool(node[3])}'
    return f'{parenthesis_start}{result}\n{quote_spaces}{parenthesis_end}'


def is_bool(item):
    if type(item) is bool:
        return str(item).lower()
    elif item is None:
        return 'null'
    else:
        return item
