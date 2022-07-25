import gendiff


def test_gendiff_json():
    assert gendiff.generate_diff_json("tests/fixtures/file1.json", "tests/fixtures/file2.json") == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_gendiff_yaml():
    assert gendiff.generate_diff_yaml("tests/fixtures/file1.yaml", "tests/fixtures/file2.yaml") == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''