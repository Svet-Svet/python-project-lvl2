from gendiff.comparison.formatters.get_format import get_formatted_output
from gendiff.comparison.parser_format import parser_file

NoValue = object()

ADDED = 'added'
REMOVED = 'removed'
IDENTICAL = 'identical'
CHANGED = 'changed'
NESTED = 'nested'


def get_diff(obj1: dict, obj2: dict) -> list:
    keys = set(obj1.keys() | obj2.keys())

    graph = []
    for key in keys:
        val1 = obj1.get(key, NoValue)
        val2 = obj2.get(key, NoValue)

        if key not in obj1:
            graph.append((ADDED, key, val2))

        elif key not in obj2:
            graph.append((REMOVED, key, val1))

        elif isinstance(val1, dict) and isinstance(val2, dict):
            graph.append((NESTED, key, get_diff(val1, val2)))

        elif val1 == val2:
            graph.append((IDENTICAL, key, val1))

        else:
            graph.append((CHANGED, key, val2, val1))

    graph.sort(key=lambda n: (n[1], n[0]))
    return graph


def get_diff_graph(obj1, obj2):
    graph = get_diff(obj1, obj2)
    graph.sort(key=lambda x: (x[1], x[0]))
    print(graph)
    return graph


def generate_diff(file1, file2, formatter='stylish'):
    data_first = parser_file(file1)
    data_second = parser_file(file2)
    graph = get_diff_graph(data_first, data_second)
    result = get_formatted_output(graph, formatter)
    return result
