from gendiff.comparison.formatters.stylish import stylish
from gendiff.comparison.formatters.plain import plain
from gendiff.comparison.formatters.json import json_format

from tests.fixtures.result_json import result_json
from tests.fixtures.result_stylish import result_stylish
from tests.fixtures.result_plain import result_plain


def test_json():
    assert json_format("tests/fixtures/file1.json") == result_json()


def test_stylish():
    assert stylish("tests/fixtures/file_deep1.json", "tests/fixtures/file_deep2.json") == result_stylish()


def test_plain():
    assert plain("tests/fixtures/file_deep1.json", "tests/fixtures/file_deep2.json") == result_plain()
