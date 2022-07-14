#!/usr/bin/env python

import os
import sys
import json
import argparse

from gendiff import generate_diff


#def abs_path('/Users/mac/python-project-lvl2/python-project-lvl2/gendiff/comparison/comparison.py'):
#    return os.path.join(os.path.dirname(os.path.abspath(__file__)), '/Users/mac/python-project-lvl2/python-project-lvl2/gendiff/comparison/comparison.py')

def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', )
    parser.add_argument('second_file', )
    parser.add_argument('-f', '--format', help='set format of output', )

    args = parser.parse_args()
    print(args.first_file)
    print(args.second_file)
    with open(args.first_file, 'r') as file:
        file1 = json.load(file)
    with open(args.second_file, 'r') as file:
        file2 = json.load(file)

    generate_diff(file1, file2)

if __name__ == '__main__':
    main()
    #print(list(map(abs_path, sys.argv[1:0])))
