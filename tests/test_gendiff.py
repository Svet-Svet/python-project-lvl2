from gendiff import generate_diff


file1 = {
  "timeout": 50
}

file2 = {
    "timeout": 50
}


def test_gendiff_good():
    assert generate_diff(file1, file2) == '{  timeout: 50 }'

