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
#             # result += f'\n{count_spaces}{key}: {stylish(value, replacer, spaces_count, _deep + 1)}
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
    parenthesis_start = "{"
    parenthesis_end = "}"
    count_spaces = replacer * spaces_count * (_deep + 2)
    quote_spaces = replacer * spaces_count * _deep
    for node in graph:
        if isinstance(node[2], list):
            if node[0] == "added":
                general_names_of_group = f'\n{count_spaces}+ {node[1]}: '
                result += general_names_of_group + stylish(node[2], replacer, spaces_count, _deep + 4)
            elif node[0] == "removed":
                general_names_of_group = f'\n{count_spaces}- {node[1]}: '
                result += general_names_of_group + stylish(node[2], replacer, spaces_count, _deep + 4)
            elif node[0] == "identical":
                general_names_of_group = f'\n{count_spaces}  {node[1]}: '
                result += general_names_of_group + stylish(node[2], replacer, spaces_count, _deep + 4)
            elif node[0] == "changed":
                general_names_of_group_old = f'\n{count_spaces}- {node[1]}: '
                general_names_of_group_new = f'\n{count_spaces}+ {node[1]}: {node[3]}'
                result += general_names_of_group_old + stylish(node[2], replacer, spaces_count, _deep + 4)
                result += general_names_of_group_new

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
