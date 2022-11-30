from gendiff.comparison.get_graph import ADDED, REMOVED, IDENTICAL, CHANGED, NESTED


# flake8: noqa: max-complexity: 10
def stylish(graph, _deep=0):
    if isinstance(graph, bool):
        return str(graph).lower()

    if graph is None:
        return 'null'

    replacer = ' '

    parenthesis_start = "{"
    parenthesis_end = "}"
    count_spaces = replacer * ((_deep * 4) + 2)
    quote_spaces = replacer * (_deep * 4)
    result = []
    if isinstance(graph, dict):
        for k, v in graph.items():
            result.append(f'{count_spaces}  {k}: {stylish(v, _deep + 1)}')
        result = '\n'.join(result)
        return f'{parenthesis_start}\n{result}\n{quote_spaces}{parenthesis_end}'

    if not isinstance(graph, list):
        return str(graph)

    for node in graph:
        status, key, *values = node
        value1 = stylish(values[0], _deep + 1)

        if status == ADDED:
            result.append(f'{count_spaces}+ {key}: {value1}')
        elif status == REMOVED:
            result.append(f'{count_spaces}- {key}: {value1}')
        elif status == IDENTICAL:
            result.append(f'{count_spaces}  {key}: {value1}')
        elif status == CHANGED:
            value2 = stylish(values[1], _deep + 1)
            result.append(f'{count_spaces}- {key}: {value1}')
            result.append(f'{count_spaces}+ {key}: {value2}')
        elif status == NESTED:
            result.append(f'{count_spaces}  {key}: {value1}')

    result = '\n'.join(result)
    return f'{parenthesis_start}\n{result}\n{quote_spaces}{parenthesis_end}'
