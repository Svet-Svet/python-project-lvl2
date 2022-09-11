#!/usr/bin/env python
import argparse

from gendiff.comparison.parser_format import generate_parser_format


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration'
                                                 ' files'
                                                 ' and shows a difference.')
    parser.add_argument('first_file', )
    parser.add_argument('second_file', )
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default='stylish',
    )

    args = parser.parse_args()
    generate_parser_format(args.first_file, args.second_file, args.format)


if __name__ == '__main__':
    main()
    # print(list(map(abs_path, sys.argv[1:0])))
