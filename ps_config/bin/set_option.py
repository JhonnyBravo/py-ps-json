#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

from ps_config import lib


def main():
    parser = argparse.ArgumentParser(
        description="""新規 option を追加、
                または既存 option の値を更新します。""")
    parser.add_argument(
        'path',
        help='config ファイルのパス')
    parser.add_argument(
        'section',
        help='section 名')
    parser.add_argument(
        'option',
        help='option 名')
    parser.add_argument(
        'value',
        help='option の値')
    args = parser.parse_args()

    lib.set_option(args.path, args.section, args.option, args.value)

if __name__ == '__main__':
    main()
