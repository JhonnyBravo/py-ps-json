#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
from ps_config import lib


def main():
    parser = argparse.ArgumentParser(
        description="config ファイルから section の一覧を取得します。")
    parser.add_argument(
        "path",
        help="config ファイルのパス。")

    args = parser.parse_args()

    config = lib.ps_config(args.path)
    result = config.get_section_list()

    if len(result) > 0:
        for i in result:
            print(i)

if __name__ == "__main__":
    main()
