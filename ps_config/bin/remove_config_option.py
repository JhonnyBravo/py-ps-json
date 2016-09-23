#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
from ps_config import lib


def main():
    parser = argparse.ArgumentParser(
        description="config ファイルから option を削除します。")
    parser.add_argument(
        "path",
        help="config ファイルのパス。")
    parser.add_argument(
        "section_name",
        help="section の名前。")
    parser.add_argument(
        "option_name",
        help="削除する option の名前。")

    args = parser.parse_args()

    config = lib.ps_config(args.path)
    config.remove_option(args.section_name, args.option_name)

if __name__ == "__main__":
    main()
