#!/usr/bin/env python
import os
import sys
from gendiff.comprasion.comparison import generate_diff


def abs_path(path):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), path)

def main():
    generate_diff('file1', 'file2')

if __name__ == '__main__':
    print(list(map(abs_path, sys.argv[1:0])))