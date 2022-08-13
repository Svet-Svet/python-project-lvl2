# from gendiff.comparison.formatters.get_format import get_format
from gendiff.comparison.formatters.stylish import stylish

ADDED = '+'
REMOVED = '-'
IDENTICAL = ' '


def value_to_string(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def get_diff_graph(file1, file2, format='stylish'):
    merged_dict = file1 | file2
    sorted_tuple = dict(sorted(merged_dict.items(), key=lambda x: x[0]))
    diff_graph = []
    for key in sorted_tuple.keys():
        value1 = value_to_string(file1.get(key))
        value2 = value_to_string(file2.get(key))

        if isinstance(value1, dict) and isinstance(value2, dict):
            sub_graph = generate_diff(value1, value2)
            diff_graph.append((IDENTICAL, key, sub_graph))

        if key not in file1.keys():
            diff_graph.append(('+', key, value2))
        else:
            if key not in file2.keys():
                diff_graph.append((REMOVED, key, value1))
            else:
                if file1.get(key) == file2.get(key):
                    diff_graph.append((IDENTICAL, key, value1))
                else:
                    diff_graph.append((REMOVED, key, value1))
                    diff_graph.append((ADDED, key, value2))
    # print(diff_graph)
    return diff_graph


def generate_diff(file1, file2, format='stylish'):
    graph = get_diff_graph(file1, file2)
    #formatter = FORMATTERS[format]
    print(stylish(graph))
    return stylish(graph)


# def generate_diff(file1, file2):
#     merged_dict = file1 | file2
#     sorted_tuple = dict(sorted(merged_dict.items(), key=lambda x: x[0]))
#     result = ''
#     for key in sorted_tuple.keys():
#         value1 = value_to_string(file1.get(key))
#         value2 = value_to_string(file2.get(key))
#         if key not in file1.keys():
#             result = f'{result}  {SIGN_NEW_DATA} {key}: {value2}\n'
#         else:
#             if key not in file2.keys():
#                 result = f'{result}  {SIGN_OLD_DATA} {key}: {value1}\n'
#             else:
#                 if file1.get(key) == file2.get(key):
#                     result = f'{result}    {key}: {value1}\n'
#                 else:
#                     result = f'{result}  {SIGN_OLD_DATA} {key}: {value1}\n'
#                     result = f'{result}  {SIGN_NEW_DATA} {key}: {value2}\n'
#     print(f'{{\n{result}}}')
#     return f'{{\n{result}}}'
