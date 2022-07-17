from gendiff import generate_diff

file1 = {
  "timeout": 50
}

file2 = {
  "timeout": 20
}

def test_gendiff():
    assert generate_diff(file1, file2) == ('{\n- timeout: 50\n+ timeout: 20}')