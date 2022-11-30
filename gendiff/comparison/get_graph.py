ADDED = 'added'
REMOVED = 'removed'
IDENTICAL = 'identical'
CHANGED = 'changed'
NESTED = 'nested'


def get_diff_graph(obj1: dict, obj2: dict) -> list:
    keys = set(obj1.keys() | obj2.keys())

    graph = []
    for key in keys:
        val1 = obj1.get(key)
        val2 = obj2.get(key)

        if key not in obj1:
            graph.append((ADDED, key, val2))

        elif key not in obj2:
            graph.append((REMOVED, key, val1))

        elif val1 == val2:
            graph.append((IDENTICAL, key, val2))

        elif isinstance(val1, dict) and isinstance(val2, dict):
            graph.append((NESTED, key, get_diff_graph(val1, val2)))

        else:
            graph.append((CHANGED, key, val1, val2))

    graph.sort(key=lambda n: (n[1], n[0]))
    return graph
