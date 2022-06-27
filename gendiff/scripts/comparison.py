#!/usr/bin/env python
import os
import sys
import json

from gendiff.comparison.comparison import generate_diff


#def abs_path('/Users/mac/python-project-lvl2/python-project-lvl2/gendiff/comparison/comparison.py'):
#    return os.path.join(os.path.dirname(os.path.abspath(__file__)), '/Users/mac/python-project-lvl2/python-project-lvl2/gendiff/comparison/comparison.py')

def main():
    with open('/Users/mac/python-project-lvl2/python-project-lvl2/gendiff/comparison/file1.json', 'r') as file:
        file1 = json.load(file)
    with open('/Users/mac/python-project-lvl2/python-project-lvl2/gendiff/comparison/file2.json', 'r') as file:
        file2 = json.load(file)

    generate_diff(file1, file2)

if __name__ == '__main__':
    main()
    #print(list(map(abs_path, sys.argv[1:0])))