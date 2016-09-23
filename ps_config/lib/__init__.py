# coding: utf-8

import ConfigParser
import os
import sys


class ps_config():

    def __init__(self, path):
        self.path = path
        self.config = ConfigParser.RawConfigParser()
        self.config.read(self.path)

    def test_path(self):
        if not os.path.exists(self.path):
            print(self.path + " は存在しません。")
            sys.exit(1)

    def get_section_list(self):
        self.test_path()
        section_list = self.config.sections()
        return section_list

    def get_option_list(self, section_name):
        self.test_path()

        if not self.config.has_section(section_name):
            print(section_name + " は存在しません。")
            sys.exit(1)

        option_list = self.config.items(section_name)
        return option_list

    def get_option_value(self, section_name, option_name):
        self.test_path()

        if not self.config.has_section(section_name):
            print(section_name + " は存在しません。")
            sys.exit(1)

        if not self.config.has_option(section_name, option_name):
            print(option_name + " は存在しません。")
            sys.exit(1)

        option_value = self.config.get(section_name, option_name)
        return option_value

    def set_content(self):
        with open(self.path, "wt") as file:
            self.config.write(file)

    def remove_section(self, section_name):
        self.test_path()
        self.config.remove_section(section_name)
        self.set_content()

    def remove_option(self, section_name, option_name):
        self.test_path()
        self.config.remove_option(section_name, option_name)
        self.set_content()

    def set_option(self, section_name, option_name, value):
        if not self.config.has_section(section_name):
            self.config.add_section(section_name)

        self.config.set(section_name, option_name, value)
        self.set_content()
