from gendiff.comparison.formatters.get_format import get_formatted_output
from gendiff.comparison.parser_format import parse_file
from gendiff.comparison.get_tree import get_diff_graph


def generate_diff(file1, file2, format_='stylish'):
    data_first = parse_file(file1)
    data_second = parse_file(file2)
    graph = get_diff_graph(data_first, data_second)
    return get_formatted_output(graph, format_)
