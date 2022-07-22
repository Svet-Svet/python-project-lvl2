import json

SIGN_NEW_DATA = '+'
SIGN_OLD_DATA = '-'


def value_to_string(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(file1, file2):
    with open(file1, 'r') as file:
        file1 = json.load(file)
    with open(file2, 'r') as file:
        file2 = json.load(file)
    merged_dict = file1 | file2
    sorted_tuple = dict(sorted(merged_dict.items(), key=lambda x: x[0]))
    result = ''
    for key in sorted_tuple.keys():
        value1 = value_to_string(file1.get(key))
        value2 = value_to_string(file2.get(key))
        if key not in file1.keys():
            result = f'{result}{SIGN_NEW_DATA} {key}: {value2}\n'
        else:
            if key not in file2.keys():
                result = f'{result}{SIGN_OLD_DATA} {key}: {value1}\n'
            else:
                if file1.get(key) == file2.get(key):
                    result = f'{result}  {key}: {value1}\n'
                else:
                    result = f'{result}{SIGN_OLD_DATA} {key}: {value1}\n'
                    result = f'{result}{SIGN_NEW_DATA} {key}: {value2}\n'
    print(f'{{\n{result}}}')
    return f'{{\n{result}}}'
