import json
SIGN_NEW_DATA = '+'
SIGN_OLD_DATA = '-'

def generate_diff(file1, file2):
  merged_dict = file1 | file2
  sorted_tuple = dict(sorted(merged_dict.items(), key=lambda x: x[0]))

  def dict_with_lowercase(sorted_tuple):
    for values in sorted_tuple.values():
      if type(values) == bool:
        values = str(values).lower()

  dict_with_lowercase(sorted_tuple)
  result = ''
  for keys in sorted_tuple.keys():
    if keys not in file1.keys():
      result = f'{result}{SIGN_NEW_DATA} {keys}: {file2.get(keys)}\n'
    else:
      if keys not in file2.keys():
        result = f'{result}{SIGN_OLD_DATA} {keys}: {file1.get(keys)}\n'
      else:
        if file1.get(keys) == file2.get(keys):
          result = f'{result}  {keys}: {file1.get(keys)}\n'
        else:
          result = f'{result}{SIGN_OLD_DATA} {keys}: {file1.get(keys)}\n'
          result = f'{result}{SIGN_NEW_DATA} {keys}: {file2.get(keys)}\n'
  print(f'{{\n{result}}}')






















  # бэклог задачи: file1_sorted = {key: file1[key] for key in sorted(file1)}
  # file2_sorted = {key: file2[key] for key in sorted(file2)}
  # print(file1_sorted)
  #
  # result = ''
  #
  # for keys, item in file1_sorted.items():
  #   if keys in file1_sorted == keys in file2_sorted.get(keys):
  #     if item in file1_sorted == item in file2_sorted.items(keys, item):
  #       result = f'{result}  {keys}: {item}\n'
  #     else:
  #       result = f'{result}{SIGN_OLD_DATA} {keys}: {item}\n{SIGN_NEW_DATA} {file2_sorted.get()}: {file2_sorted.get()}\n'
  #   else:
  #     result = f'{result}{SIGN_OLD_DATA} {keys}: {item}\n{SIGN_NEW_DATA} {file2_sorted.get(keys, item)}: {file2_sorted.get(keys, item)}\n'
  # print(f'{{\n{result}}}')

  #for i in dict1:
  #  if (i in dict2) and (dict1[i] == dict2[i]):
  #    shared_dict[i] = dict1[i]


  # for keys1, item1 in file1_sorted.items():
  #   for keys2, item2 in file2_sorted.items():
  #     if keys1 in file1_sorted.keys() == keys2 in file2_sorted.keys():
  #       if item1 in file1_sorted.values() == item2 in file2_sorted.keys():
  #         result = f'{result}  {keys1}: {item1}\n'
  #       else:
  #         result = f'{result}{SIGN_OLD_DATA} {keys1}: {item1}\n{SIGN_NEW_DATA} {keys2}: {item2}\n'
  #     else:
  #       result = f'{result}{SIGN_OLD_DATA} {keys1}: {item1}\n{SIGN_NEW_DATA} {keys2}: {item2}\n'
  # print(f'{{\n{result}}}')