#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
from ps_json import lib


def main():
    parser = argparse.ArgumentParser(
        description="json ファイルから key の値を取得します。")
    parser.add_argument(
        "path",
        help="json ファイルのパス。")
    parser.add_argument(
        "key_name",
        help="値を取得する key の名前。")

    args = parser.parse_args()
    result = lib.get_key_value(args.path,args.key_name)

    print(result)

if __name__ == "__main__":
    main()
