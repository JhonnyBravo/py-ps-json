#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
from ps_config import lib


def main():
    parser = argparse.ArgumentParser(
        description="config ファイルへ option を設定します。")
    parser.add_argument(
        "path",
        help="config ファイルのパス。")
    parser.add_argument(
        "section_name",
        help="option を設定する section の名前。")
    parser.add_argument(
        "option_name",
        help="値を設定する option の名前。")
    parser.add_argument(
        "value",
        help="option へ設定する値。")

    args = parser.parse_args()

    config=lib.ps_config(args.path)
    config.set_option(args.section_name,args.option_name,args.value)

if __name__ == "__main__":
    main()
