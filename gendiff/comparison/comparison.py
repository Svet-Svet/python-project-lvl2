from gendiff.comparison.get_format import get_format
from gendiff.comparison.parser_format import generate_parser_format

ADDED = '+'
REMOVED = '-'
IDENTICAL = ' '
CHANGED = '*'


def value_to_string(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


NoValue = object()


# flake8: noqa: max-complexity: 10
def get_diff(key, obj1, obj2):
    val1 = obj1.get(key, NoValue)
    val2 = obj2.get(key, NoValue)

    if isinstance(val1, dict) and isinstance(val2, dict):
        subkeys = set(sorted(val1.keys() | val2.keys()))
        subgraph = []
        for subkey in sorted(subkeys):
            subgraph.extend(get_diff(subkey, val1, val2))
        return add_note("identical", key, subgraph)

    elif isinstance(val1, dict) and val2 is not NoValue:
        subgraph = []
        for subkey in val1.keys():
            subgraph.extend(get_diff(subkey, val1, val1))
        status = "changed"
        return [(status, key, subgraph, val2)]

    elif isinstance(val2, dict) and val1 is not NoValue:
        subgraph = []
        for subkey in val2.keys():
            subgraph.extend(get_diff(subkey, val2, val2))
        status = "changed"
        return [(status, key, val1, subgraph)]

    elif isinstance(val1, dict):
        subgraph = []
        for subkey in val1.keys():
            subgraph.extend(get_diff(subkey, val1, val1))
        return add_note("removed", key, subgraph)

    elif isinstance(val2, dict):
        subgraph = []
        for subkey in val2.keys():
            subgraph.extend(get_diff(subkey, val2, val2))
        result = []
        if val1 is not NoValue:
            status = "removed"
            result.append((status, key, val1))

        status = "added"
        result.append((status, key, subgraph))
        return result
    elif val1 is NoValue:
        return add_note("added", key, val2)
    elif val2 is NoValue:
        return add_note("removed", key, val1)
    elif val1 == val2:
        return add_note('identical', key, val1)
    else:
        status = "changed"
        return [(status, key, val1, val2)]


def add_note(status, key, val):
    result = [(status, key, val)]
    return result


def get_diff_graph(obj1, obj2):
    graph = []
    keys = set(obj1.keys() | obj2.keys())

    for key in keys:
        graph.extend(get_diff(key, obj1, obj2))

    graph.sort(key=lambda x: (x[1], x[0]))
    return graph


def generate_diff(file1, file2, formatter='stylish'):
    file1_open = generate_parser_format(file1)
    file2_open = generate_parser_format(file2)
    graph = get_diff_graph(file1_open, file2_open)
    result = get_format(graph, formatter)
    return result
