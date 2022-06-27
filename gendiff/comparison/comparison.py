
SIGN_NEW_DATA = '+'
SIGN_OLD_DATA = '-'

def generate_diff(file1, file2):
  file1_sorted = {key: file1[key] for key in sorted(file1)}
  file2_sorted = {key: file2[key] for key in sorted(file2)}

  result = ''

  for keys1, item1 in file1_sorted.items():
    for keys2, item2 in file2_sorted.items():
      if keys1 in file1_sorted.keys() == keys2 in file2_sorted.keys():
        if item1 in file1_sorted.values() == item2 in file2_sorted.keys():
          result = f'{result}  {keys1}: {item1}\n'
        else:
          result = f'{result}{SIGN_OLD_DATA} {keys1}: {item1}\n{SIGN_NEW_DATA} {keys2}: {item2}\n'
      else:
        result = f'{result}{SIGN_OLD_DATA} {keys1}: {item1}\n{SIGN_NEW_DATA} {keys2}: {item2}\n'
  print(f'{{\n{result}}}')


