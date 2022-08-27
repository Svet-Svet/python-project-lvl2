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
                _old_value = node[2]
                _new_value = node[0]
                if _new_value == '+':
                    result += f"Property '{'.'.join(prefix_paths)}' was updated. From '{_old_value}' to '{node[2]}\n'"
                else:
                    result += f"Property '{'.'.join(prefix_paths)}' was removed\n"
            elif node[0] == '+':
                result += f"Property '{'.'.join(prefix_paths)}' was added with value: {node[2]}\n"
    print(result)
    return result
