# coding: utf-8

import ConfigParser

config = ConfigParser.RawConfigParser()


def get_sections(path):
    config.read(path)
    section_list = config.sections()

    return section_list


def get_options(path, section):
    config.read(path)
    option_list = config.items(section)

    return option_list


def get_option(path, section, option):
    config.read(path)
    option_value = config.get(section, option)

    return option_value


def remove_section(path, section):
    config.read(path)
    config.remove_section(section)

    with open(path, 'wt') as file:
        config.write(file)


def remove_option(path, section, option):
    config.read(path)
    config.remove_option(section, option)

    with open(path, 'wt') as file:
        config.write(file)


def set_option(path, section, option, value):
    config.read(path)

    if not config.has_section(section):
        config.add_section(section)

    config.set(section, option, value)

    with open(path, 'wt') as file:
        config.write(file)
