#!/usr/bin/env python
import argparse
import os.path

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
    if os.path.splitext(args.first_file[-4:]) == 'json':
        gendiff.generate_diff_json(args.first_file, args.second_file)
    else:
        gendiff.generate_diff_yaml(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
    # print(list(map(abs_path, sys.argv[1:0])))
