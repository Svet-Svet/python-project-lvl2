#!/usr/bin/env python
import json
import argparse

import gendiff


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration'
                                                 ' files'
                                                 ' and shows a difference.')
    parser.add_argument('first_file', )
    parser.add_argument('second_file', )
    parser.add_argument('-f', '--format', help='set format of output', )

    args = parser.parse_args()
    print(args.first_file)
    print(args.second_file)
    # with open(args.first_file, 'r') as file:
    #     file1 = json.load(file)
    # with open(args.second_file, 'r') as file:
    #     file2 = json.load(file)

    gendiff.generate_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
    # print(list(map(abs_path, sys.argv[1:0])))
