from gendiff.comparison.formatters.formats import get_formatted_output
from gendiff.comparison.parser_format import parse_file
from gendiff.comparison.graph import get_diff_graph
from gendiff.comparison.formatters.formats import DEFAULT_FORMAT


def generate_diff(file1, file2, format_=DEFAULT_FORMAT):
    data_first = parse_file(file1)
    data_second = parse_file(file2)
    graph = get_diff_graph(data_first, data_second)
    return get_formatted_output(graph, format_)
