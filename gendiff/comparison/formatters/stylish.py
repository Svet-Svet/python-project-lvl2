from gendiff.comparison.constants_status import ADDED, REMOVED, IDENTICAL, CHANGED


# flake8: noqa: max-complexity: 10
def stylish(graph, _deep=0):
    replacer = ' '
    result = []
    parenthesis_start = "{"
    parenthesis_end = "}"
    count_spaces = replacer * (_deep + 2)
    quote_spaces = replacer * _deep
    for node in graph:
        status, key, *values = node
        value = check_bool(node[2])
        if isinstance(node[2], list):
            if status == ADDED:
                keys = f'\n{count_spaces}+ {node[1]}: '
                result.append(keys + stylish(value, _deep + 4))
            elif status == REMOVED:
                keys = f'\n{count_spaces}- {node[1]}: '
                result.append(keys + stylish(value, _deep + 4))
            elif status == IDENTICAL:
                keys = f'\n{count_spaces}  {node[1]}: '
                result.append(keys + stylish(value, _deep + 4))
            elif status == CHANGED:
                value_new = check_bool(node[3])
                old = f'\n{count_spaces}- {node[1]}: '
                new = f'\n{count_spaces}+ {node[1]}: {value_new}'
                result.append(old + stylish(value, _deep + 4))
                result.append(new)
        elif status == CHANGED and isinstance(node[3], list):
                old = f'\n{count_spaces}- {node[1]}: {value}'
                new = f'\n{count_spaces}+ {node[1]}: '\
                      + stylish(node[3], _deep + 4)
                result.append(old)
                result.append(new)
        elif status == ADDED:
            result.append(f'\n{count_spaces}+ {node[1]}: {value}')
        elif status == REMOVED:
            result.append(f'\n{count_spaces}- {node[1]}: {value}')
        elif status == IDENTICAL:
            result.append(f'\n{count_spaces}  {node[1]}: {value}')
        elif status == CHANGED:
            value_new = check_bool(node[3])
            result.append(f'\n{count_spaces}- {node[1]}: {value}')
            result.append(f'\n{count_spaces}+ {node[1]}: {value_new}')
    result = ''.join(result)
    return f'{parenthesis_start}{result}\n{quote_spaces}{parenthesis_end}'


def check_bool(item):
    if type(item) is bool:
        return str(item).lower()
    elif item is None:
        return 'null'
    else:
        return item
