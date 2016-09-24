#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
from ps_json import lib


def main():
    parser = argparse.ArgumentParser(
        description="json ファイルから key を削除します。")
    parser.add_argument(
        "path",
        help="json ファイルのパス。")
    parser.add_argument(
        "key_name",
        help="削除する key の名前。")

    args = parser.parse_args()
    lib.remove_key(args.path, args.key_name)

if __name__ == "__main__":
    main()
