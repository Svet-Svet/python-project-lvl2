# def stylish(node, replacer=' ', spaces_count=3, _deep=0):
#     if type(node) is dict:
#         result = ''
#         parenthesis_start = "{"
#         parenthesis_end = "}"
#         count_spaces = replacer * spaces_count * (_deep + 1)
#         quote_spaces = replacer * spaces_count * _deep
#
#         for key, vallue in node.items():
#             result += f'\n{count_spaces}{key}: {stylish(vallue, replacer, spaces_count, _deep + 1)}'
#         return f'{parenthesis_start}{result}\n{quote_spaces}{parenthesis_end}'
#     return str(node)


def stylish(graph, replacer=' ', spaces_count=3, _deep=0):
    result = ''
    parenthesis_start = "{"
    parenthesis_end = "}"
    count_spaces = replacer * spaces_count * (_deep + 1)
    quote_spaces = replacer * spaces_count * _deep
    for node in graph:
        if isinstance(node[2], dict):
            result += stylish(node[2])
            # result += f'\n{count_spaces}{key}: {stylish(vallue, replacer, spaces_count, _deep + 1)}
        else:
            # out += '\n' + ' '.join(node)
            result += f'\n {node}'
    return result

