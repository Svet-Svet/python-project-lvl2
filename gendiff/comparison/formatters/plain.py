import json

ADDED = 'added'
REMOVED = 'removed'
IDENTICAL = 'identical'
CHANGED = 'changed'


# flake8: noqa: max-complexity: 10
def plain(graph, prefix_paths=None):
    result = []
    prefix_paths = prefix_paths or []
    for node in graph:
        status, key, *values = node
        _paths = prefix_paths + [key]
        if isinstance(values[0], list) and status == IDENTICAL:
            result.extend(plain(values[0], prefix_paths=_paths))
        else:
            if status == REMOVED:
                result.append(f"Property '{'.'.join(_paths)}' was removed")
            elif status == ADDED:
                value = format_value(values[0])
                result.append(f"Property '{'.'.join(_paths)}'"
                              f" was added with value: {value}")
            elif status == CHANGED:
                old_value = format_value(values[0])
                new_value = format_value(values[1])
                result.append(
                    f"Property '{'.'.join(_paths)}'"
                    f" was updated. From {old_value} to {new_value}")
    if len(prefix_paths) == 0:
        return '\n'.join(result)
    return result


def format_value(value_):
    if isinstance(value_, bool) or value_ is None or isinstance(value_, int):
        new_value = json.dumps(value_)
        return f"{new_value}"
    elif isinstance(value_, list):
        return '[complex value]'
    else:
        return f"'{value_}'"
