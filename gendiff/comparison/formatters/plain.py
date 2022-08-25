def plain(graph, replacer=' ', spaces_count=1, _deep=0):
    result = ''
    parenthesis_start = "{"
    parenthesis_end = "}"
    count_spaces = replacer * spaces_count * (_deep + 1)
    quote_spaces = replacer * spaces_count * _deep
    for node in graph:
        if isinstance(node[2], list):
            general_names_of_group = f'\n{count_spaces}{node[0]} {node[1]}: '
            result += general_names_of_group + plain(node[2], replacer, spaces_count, _deep + 4)
            # result += f'\n{count_spaces}{key}: {stylish(vallue, replacer, spaces_count, _deep + 1)}
        else:
            result += f'\n{count_spaces}{node[0]} {node[1]}: {node[2]} '
            # count_spaces += " "
    return f'{parenthesis_start}{result}\n{quote_spaces}{parenthesis_end}'
