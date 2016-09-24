#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
from ps_json import lib


def main():
    parser = argparse.ArgumentParser(
        description="json ファイルから key の一覧を取得します。")
    parser.add_argument(
        "path",
        help="json ファイルのパス。")
    args = parser.parse_args()

    result = lib.get_key_list(args.path)

    if len(result) > 0:
        for i in result:
            print(i)

if __name__ == "__main__":
    main()
