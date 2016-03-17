#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

from ps_config import lib


def main():
    parser = argparse.ArgumentParser(
        description='config ファイルから section の一覧を取得します。')
    parser.add_argument(
        'path',
        help='config ファイルのパス')
    args = parser.parse_args()

    section_list = lib.get_sections(args.path)

    for section in section_list:
        print(section)

if __name__ == '__main__':
    main()
