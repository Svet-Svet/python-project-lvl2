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


def test_gendiff_deep_json():
    assert gendiff.generate_diff_json("tests/fixtures/file_deep1.json", "tests/fixtures/file_deep2.json") == '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow:
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''


def test_gendiff_deep_yaml():
    assert gendiff.generate_diff_yaml("tests/fixtures/file_deep1.yaml", "tests/fixtures/file_deep2.yaml") == '''{
    common:
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5:
            key5: value5
        setting6:
            doge:
              - wow:
              + wow: so much
            key: value
          + ops: vops
    group1:
      - baz: bas
      + baz: bars
        foo: bar
      - nest:
            key: value
      + nest: str
  - group2:
        abc: 12345
        deep:
            id: 45
  + group3:
        deep:
            id:
                number: 45
        fee: 100500
}'''