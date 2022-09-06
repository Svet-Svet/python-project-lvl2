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
    elif isinstance(val1, dict) and val2 is not NoValue:
        subgraph = []
        for subkey in val1.keys():
            subgraph.extend(get_diff(subkey, val1, val1))
        status = "changed"
        return [(status, key, subgraph, val2)]

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


def generate_diff(file1, file2, format='stylish'):
    graph = get_diff_graph(file1, file2)
    result = plain(graph)
    print(result)
    return result
