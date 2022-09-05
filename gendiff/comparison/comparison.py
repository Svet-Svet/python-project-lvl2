from gendiff.comparison.formatters.plain import plain

ADDED = '+'
REMOVED = '-'
IDENTICAL = ' '
CHANGED = '*'


def value_to_string(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


NoValue = object()

# АЛЬТЕРНАТИВНАЯ ФУНКЦИЯ
# def get_diff(key, obj1, obj2):
#     val1 = value_to_string(obj1.get(key, NoValue))
#     val2 = value_to_string(obj2.get(key, NoValue))
#
#     if isinstance(val1, dict) and isinstance(val2, dict):
#         subkeys = set(sorted(val1.keys() | val2.keys()))
#         subgraph = []
#         for subkey in subkeys:
#             subgraph.extend(get_diff(subkey, val1, val2))
#
#         return [
#             ({'status': IDENTICAL,
#             'key': key,
#             'value': subgraph})
#         ]
#     elif isinstance(val1, dict):
#         subgraph = []
#         for subkey in val1.keys():
#             subgraph.extend(get_diff(subkey, val1, val1))
#
#         result = [
#             ({'status': REMOVED,
#             'key': key,
#             'value': subgraph}),
#         ]
#         if val2 is not NoValue:
#             result.append(({'status': ADDED, 'key': key, 'value': val2}))
#         return result
#     elif isinstance(val2, dict):
#         subgraph = []
#         for subkey in val2.keys():
#             subgraph.extend(get_diff(subkey, val2, val2))
#
#         result = [
#             ({'status': ADDED,
#             'key': key,
#             'value': subgraph}),
#         ]
#         if val1 is not NoValue:
#             result.append(({'status': REMOVED, 'key': key, 'value': val1}))
#         return result
#     elif val1 is NoValue:
#         return [
#             ({'status': ADDED,
#             'key': key,
#             'value': val2})
#         ]
#     elif val2 is NoValue:
#         return [
#             ({'status': REMOVED, 'key': key, 'value': val1})
#         ]
#
#     if val1 == val2:
#         return [({'status': IDENTICAL, 'key': key, 'value': val1})]
#
#     return [
#         ({'status': REMOVED, 'key': key, 'value': val1}),
#         ({'status': ADDED, 'key': key, 'value': val2})
#     ]


def get_diff(key, obj1, obj2):
    val1 = value_to_string(obj1.get(key, NoValue))
    val2 = value_to_string(obj2.get(key, NoValue))

    if isinstance(val1, dict) and isinstance(val2, dict):
        subkeys = set(sorted(val1.keys() | val2.keys()))
        subgraph = []
        for subkey in sorted(subkeys):
            subgraph.extend(get_diff(subkey, val1, val2))

        status = 'identical'
        return [
            (status, key, subgraph)
        ]
    elif isinstance(val1, dict):
        subgraph = []
        for subkey in val1.keys():
            subgraph.extend(get_diff(subkey, val1, val1))

        status = "removed"
        result = [
            (status, key, subgraph),
        ]
        if val2 is not NoValue:
            status = "added"
            result.append((status, key, val2))
        return result
    elif isinstance(val2, dict):
        subgraph = []
        for subkey in val2.keys():
            subgraph.extend(get_diff(subkey, val2, val2))

        status = "added"
        result = [
            (status, key, subgraph),
        ]
        if val1 is not NoValue:
            status = "removed"
            result.append((status, key, val1))
        return result
    elif val1 is NoValue:
        status = "added"
        return [
            (status, key, val2)
        ]
    elif val2 is NoValue:
        status = "removed"
        return [
            (status, key, val1)
        ]

    if val1 == val2:
        status = "identical"
        return [(status, key, val1)]

    else:
        status = "changed"
        return [(status, key, val1, val2)]


def get_diff_graph(obj1, obj2):
    graph = []
    keys = set(obj1.keys() | obj2.keys())

    for key in keys:
        graph.extend(get_diff(key, obj1, obj2))

    graph.sort(key=lambda x: (x[1], x[0]))
    print(graph)

    return graph

# def get_diff_graph(file1, file2, format='stylish'):
#     merged_dict = file1 | file2
#     sorted_tuple = dict(sorted(merged_dict.items(), key=lambda x: x[0]))
#     diff_graph = []
#     for key in sorted_tuple.keys():
#         value1 = value_to_string(file1.get(key))
#         value2 = value_to_string(file2.get(key))
#
#         if isinstance(value1, dict) and isinstance(value2, dict):
#             sub_graph = get_diff_graph(value1, value2)
#             diff_graph.append((IDENTICAL, key, sub_graph))
#
#         if key not in file1.keys():
#             diff_graph.append(('+', key, value2))
#         else:
#             if key not in file2.keys():
#                 diff_graph.append((REMOVED, key, value1))
#             else:
#                 if file1.get(key) == file2.get(key):
#                     diff_graph.append((IDENTICAL, key, value1))
#                 else:
#                     diff_graph.append((REMOVED, key, value1))
#                     diff_graph.append((ADDED, key, value2))
#     # print(diff_graph)
#     return diff_graph


def generate_diff(file1, file2, format='stylish'):
    graph = get_diff_graph(file1, file2)
    result = plain(graph)
    print(result)
    return result
    # print(get_format(graph, format='stylish'))
    # return get_format(graph, format='stylish')


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
