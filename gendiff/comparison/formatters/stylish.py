
def stylish(graph, replacer=' ', spaces_count=1, _deep=0):
    result = ''
    parenthesis_start = "{"
    parenthesis_end = "}"
    count_spaces = replacer * spaces_count * (_deep + 2)
    quote_spaces = replacer * spaces_count * _deep
    for node in graph:
        if isinstance(node[2], list):
            if node[0] == "added":
                keys = f'\n{count_spaces}+ {node[1]}: '
                result += \
                    keys + stylish(node[2], replacer, spaces_count, _deep + 4)
            elif node[0] == "removed":
                keys = f'\n{count_spaces}- {node[1]}: '
                result += \
                    keys + stylish(node[2], replacer, spaces_count, _deep + 4)
            elif node[0] == "identical":
                keys = f'\n{count_spaces}  {node[1]}: '
                result += \
                    keys + stylish(node[2], replacer, spaces_count, _deep + 4)
            elif node[0] == "changed":
                old = f'\n{count_spaces}- {node[1]}: '
                new = f'\n{count_spaces}+ {node[1]}: {node[3]}'
                result += \
                    old + stylish(node[2], replacer, spaces_count, _deep + 4)
                result += new

        elif node[0] == "added":
            result += f'\n{count_spaces}+ {node[1]}: {node[2]} '
        elif node[0] == "removed":
            result += f'\n{count_spaces}- {node[1]}: {node[2]} '
        elif node[0] == "identical":
            result += f'\n{count_spaces}  {node[1]}: {node[2]} '
        elif node[0] == "changed":
            result += f'\n{count_spaces}- {node[1]}: {node[2]} '
            result += f'\n{count_spaces}+ {node[1]}: {node[3]} '
    return f'{parenthesis_start}{result}\n{quote_spaces}{parenthesis_end}'
