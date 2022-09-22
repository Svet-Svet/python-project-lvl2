import json


def plain(graph, prefix_paths=None):
    result = []
    prefix_paths = prefix_paths or []
    for node in graph:
        status, key, *values = node
        _paths = prefix_paths + [key]
        if isinstance(values[0], list) and status == "identical":
            result.extend(plain(values[0], prefix_paths=_paths))
        else:
            if status == "removed":
                result.append(f"Property '{'.'.join(_paths)}' was removed\n")
            elif status == "added":
                value = complex_value(values[0])
                result.append(f"Property '{'.'.join(_paths)}'"
                              f" was added with value: {value}\n")
            elif status == "changed":
                old_value = complex_value(values[0])
                new_value = complex_value(values[1])
                result.append(
                    f"Property '{'.'.join(_paths)}'"
                    f" was updated. From {old_value} to {new_value}\n")
    return ''.join(result).replace('True', 'true')\
        .replace('False', 'false').replace('None', 'null')


def complex_value(value_):
    if isinstance(value_, bool) or value_ is None or isinstance(value_, int):
        new_value = json.dumps(value_)
        return f"{new_value}"
    elif isinstance(value_, list):
        return '[complex value]'
    else:
        return f"'{value_}'"
