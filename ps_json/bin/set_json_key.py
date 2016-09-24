#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
from ps_json import lib


def main():
    parser = argparse.ArgumentParser(
        description="json ファイルへ key を設定します。")
    parser.add_argument(
        "path",
        help="json ファイルのパス。")
    parser.add_argument(
        "key_name",
        help="値を設定する key の名前。")
    parser.add_argument(
        "value",
        help="key へ設定する値。")

    args = parser.parse_args()
    lib.set_key(args.path, args.key_name, args.value)

if __name__ == "__main__":
    main()
