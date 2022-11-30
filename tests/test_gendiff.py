from gendiff.comparison.comparison import generate_diff
import pytest
import os


TEST_PATH = os.path.dirname(os.path.abspath(__file__))
FIXTURE_PATH = f'{TEST_PATH}/fixtures/'


def generate_test_path(path):
    return f'{FIXTURE_PATH}{path}'


@pytest.mark.parametrize('file1, file2, format_name, result', [
    ('file_deep1.json', 'file_deep2.json', 'stylish', 'result_stylish.txt'),
    ('file_deep1.yml', 'file_deep2.yml', 'stylish', 'result_stylish.txt'),
    ('file_deep1.json', 'file_deep2.json', 'plain', 'result_plain.txt'),
    ('file_deep1.yml', 'file_deep2.yml', 'plain', 'result_plain.txt')
])
def test_generate_diff(file1, file2, format_name, result):
    file1_path = generate_test_path(file1)
    file2_path = generate_test_path(file2)
    result_path = generate_test_path(result)
    with open(result_path) as file:
        expected = file.read()
        assert generate_diff(file1_path, file2_path, format_name) == expected
