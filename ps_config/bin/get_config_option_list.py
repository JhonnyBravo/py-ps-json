#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
from ps_config import lib


def main():
    parser = argparse.ArgumentParser(
        description="""
            config ファイルの指定した section から
            option の一覧を取得します。
            """)
    parser.add_argument(
        "path",
        help="config ファイルのパス。")
    parser.add_argument(
        "section_name",
        help="section の名前。")

    args = parser.parse_args()

    config=lib.ps_config(args.path)
    result=config.get_option_list(args.section_name)

    if len(result)>0:
        for i in result:
            print(i[0]+" = "+i[1])

if __name__ == "__main__":
    main()
