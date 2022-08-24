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


# АЛЬТЕРНАТИВНАЯ ФУНКЦИЯ
# def stylish(graph, replacer=' ', spaces_count=1, _deep=0):
#     result = ''
#     parenthesis_start = "{"
#     parenthesis_end = "}"
#     count_spaces = replacer * spaces_count * (_deep + 1)
#     quote_spaces = replacer * spaces_count * _deep
#     for node in graph:
#         if isinstance(node, list):
#             result += stylish(node, replacer, spaces_count, _deep + 1)
#             # result += f'\n{count_spaces}{key}: {stylish(vallue, replacer, spaces_count, _deep + 1)}
#         else:
#             for key, val in sorted(node.items()):
#                 # if node == '-' or node == '-' or node == '+':
#                 if key == 'status':
#                     # result += f'{count_spaces}{node} '
#                     result += f'{count_spaces}{val} '
#                 elif key == 'key':
#                     result += f'{val}: '
#                 elif key == 'value':
#                     result += f'{val}'
#             # result += f'{count_spaces}{node}'
#             # count_spaces += " "
#     return f'{parenthesis_start}\n {result}\n{quote_spaces}{parenthesis_end}'


def stylish(graph, replacer=' ', spaces_count=1, _deep=0):
    result = ''
    result_start = ''
    parenthesis_start = "{"
    parenthesis_end = "}"
    count_spaces = replacer * spaces_count * (_deep + 1)
    quote_spaces = replacer * spaces_count * _deep
    for node in graph:
        if isinstance(node[2], list):
            general_names_of_group = f'\n{count_spaces}{node[0]} {node[1]}: '
            result += general_names_of_group + stylish(node[2], replacer, spaces_count, _deep + 4)
            # result += f'\n{count_spaces}{key}: {stylish(vallue, replacer, spaces_count, _deep + 1)}
        else:
            result += f'\n{count_spaces}{node[0]} {node[1]}: {node[2]} '
            # count_spaces += " "
    return f'{parenthesis_start}{result}\n{quote_spaces}{parenthesis_end}'


# result += f'{{\n{count_spaces}{node}: {(node)}}}'



