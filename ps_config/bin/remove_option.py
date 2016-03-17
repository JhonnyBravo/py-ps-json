#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

from ps_config import lib


def main():
    parser = argparse.ArgumentParser(
        description='option を削除します。')
    parser.add_argument(
        'path',
        help='config ファイルのパス')
    parser.add_argument(
        'section',
        help='section 名')
    parser.add_argument(
        'option',
        help='option 名')
    args = parser.parse_args()

    lib.remove_option(args.path, args.section, args.option)

if __name__ == '__main__':
    main()
