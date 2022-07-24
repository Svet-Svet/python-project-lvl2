import gendiff


def test_gendiff_good():
    assert gendiff.generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json") == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


# def test_gendiff_with_file(file):
#     with open(file, 'r') as file:
#         file1 = json.load(file)