#!/usr/bin/env python3
"""
Emerge for BlackArch Linux

Download and compile packages from BlackArch github repo
"""
###############################################################################
#
#  Blackman - Emerge for BlackArch
#  Copyright (C) 2019  Stefan Venz
#  Copyright (C) 2019  BlackArch Linux
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  This is based on the original blackman
#  <https://github.com/BlackArch/blackman>
#
#  Original Authors:
#  nrz@nullsecurity.net
#  noptrix@nullsecurity.net
#
###############################################################################

import argparse
import subprocess
import sys

from pathlib import Path

VERSION = '0.1'

HOME = str(Path.home())
BLACKARCH_REPO = 'github'
BLACKARCH_CONFIG = HOME + '/.config/blackman/config'
LOCAL_REPO = HOME + '/.config/blackman/repo/'

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

def print_version():
    """
    print blackman version
    """
    print(VERSION)


def check_config_dir():
    """
    Check if the config directory already exists

    Arguments:
        path(str) - path for config directory
    """
    print(LOCAL_REPO)


def create_config_dir():
    """
    Create config dir
    """
    try:
        err = subprocess.run(['mkdir', '-p', LOCAL_REPO], stderr=subpress.PIPE)
        return EXIT_SUCCESS
    except:
        print("Could not create {}".format(LOCAL_REPO))
        print(err.stderr.decode('utf-8'))
        return EXIT_FAILURE


def get_pkgbuild_files():
    """
    Clone Blackarch Repo
    """
    try:
        err = subprocess.run(['git', 'clone', BLACKARCH_REPO], stderr=subprocess.PIPE)
    except:
        print("Could not clone {}".format(BLACKARCH_REPO))
        print(err.stderr.decode('utf-8'))
        return EXIT_FAILURE
    return EXIT_SUCCESS


def get_dependecies(pkg, path=BLACKARCH_REPO):
    """
    Get a list of dependencies for pkg

    Arguments:
        pkg(str) - package to be build
        path(str) - path to config

    Return:
        dep(list) - list of deo
    """
    pkg_build = path + 'packages/' + pkg + 'PKGBUILD'
    try:
        with open(pkg_build):
            print('read dependencies here')
    except:
        print("Could not open {}".format(pkg_build))


def read_from_config():
    """
    Retrieve information from config file
    """
    try:
        with open(BLACKARCH_CONFIG):
            print("read repo location from config")
    except:
        print("Could not read from {}".format(BLACKARCH_CONFIG))


def write_to_config_file():
    """
    Save variables to config file
    """
    ret = EXIT_SUCCESS
    try:
        with open(BLACKARCH_CONFIG):
            print("write to {} here".format(BLACKARCH_CONFIG))
    except:
        print("Could not write to {}".format(BLACKARCH_CONFIG))
        ret = EXIT_FAILURE

    return ret

def list_groups():
    """
    Print all BlackArch Linux groups
    """
    ret = EXIT_SUCCESS
    try:
        p = subprocess.run(['pacman', '-Sg', '|', 'grep', 'blackarch'],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        err = p.communicate()
    except:
        print("Something went wrong fetching BlackArch groups")
        print(err)
        ret = EXIT_FAILURE

    return ret




def parse_arguments():
    """
    parse command line options

    return:
        args(dict) - dict of command line options
    """
    global LOCAL_REPO

    ap = argparse.ArgumentParser()

    # package options
    ap.add_argument("-D", "--default", required=False,
                    help="Change main repo location to <path>",
                    metavar='<path>')
    ap.add_argument("-i", "--install", required=False,
                    help="install <pkg>", metavar='<pkg>', nargs='+')
    ap.add_argument("-a", "--all", required=False,
                    help="install all packages from all groups",
                    metavar='', action='append_const', const=1)
    ap.add_argument("-g", "--group", required=False,
                    help="install all packages from <group>",
                    metavar='<group>', nargs='+')
    ap.add_argument("-s", "--search", required=False,
                    help="search for <pkg>", metavar='<pkg>')

    # Additional options
    ap.add_argument("-V", "--version", required=False,
                    help="print blackman version",
                    metavar='', action='append_const', const=1)
    ap.add_argument("-v", "--verbose", required=False,
                    help="print verbose options", metavar='',
                    action='append_const', const=1)

    # Repo options
    ap.add_argument("-l", "--list", required=False,
                    help="list all blackarch groups",
                    metavar='', action='append_const', const=1)
    ap.add_argument("-p", "--packages", required=False,
                    help="list all packages from <group>",
                    metavar='<group>', nargs='+')

    args = vars(ap.parse_args())

    if len(sys.argv) < 2:
        ap.print_help()
        sys.exit(1)

    return args


def handle_args(args):
    """
    Handle command line arguments

    Arguments:
        args(dict) - command line arguments dictionary
    """
    print(args)


def main():
    """
    main function of blackman
    """
    args = parse_arguments()
    handle_args(args)


if __name__ == "__main__":
    main()
