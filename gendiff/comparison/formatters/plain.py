import json


def plain(graph, prefix_paths=None):
    result = ''
    prefix_paths = prefix_paths or []
    for node in graph:
        if isinstance(node[2], list):
            plain(node[2], prefix_paths=prefix_paths + [node[1]])
        else:
            if node[0] == ' ':
                continue
            elif node[0] == '-':
                if len(node) == 3:
                    _old_value = complex_value(node[-1])
                    _new_value = complex_value(node[-2])
                    result += f"Property '{'.'.join(prefix_paths)}' was updated. From '{_old_value}' to '{node[2]}\n'"
                else:
                    result += f"Property '{'.'.join(prefix_paths)}' was removed\n"
            elif node[0] == '+':
                value = complex_value(node[2])
                result += f"Property '{'.'.join(prefix_paths)}' was added with value: {value}\n"
    print(result)
    return result


def complex_value(value_):
    if isinstance(value_, bool) or value_ is None or isinstance(value_, int):
        new_value = json.dumps(value_)
        return f"{new_value}"
    elif isinstance(value_, dict):
        return '[complex value]'
    else:
        return f"'{value_}'"
