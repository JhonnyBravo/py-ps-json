#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

from ps_config import lib


def main():
    parser = argparse.ArgumentParser(
        description="""指定した section に属する option の一覧、
                または 特定の option の値を取得します。""")
    parser.add_argument(
        'path',
        help='config ファイルのパス')
    parser.add_argument(
        'section',
        help='option の一覧 / 値を取得したい section 名')
    parser.add_argument(
        '--option',
        help='値を取得したい option 名')
    args = parser.parse_args()

    if args.option:
        option_value = lib.get_option(args.path, args.section, args.option)
        print(option_value)
    else:
        option_list = lib.get_options(args.path, args.section)

        for option in option_list:
            print(option)

if __name__ == '__main__':
    main()
