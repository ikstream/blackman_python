#!/usr/bin/env python3
"""
Emerge for BlackArch Linux

Download and compile packages from BlackArch github repo
"""
###############################################################################
#
#  Blackman - Emerge for BlackArch
#
#  Copyright (C) 2019  BlackArch Linux
#  Copyright (C) 2019  Stefan Venz
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
import os
import subprocess
import sys

from pathlib import Path

VERSION = '0.1'

HOME = str(Path.home())
BLACKARCH_REPO = 'https://github.com/BlackArch/blackarch.git'
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

    return:
        0 if exists, 1 else
    """
    exit_no_check = 2
    try:
        if os.path.exists(BLACKARCH_CONFIG):
            ret = EXIT_SUCCESS
        else:
            ret = EXIT_FAILURE
    except:
        print("Could not check if {} exists".format(BLACKARCH_CONFIG))
        ret = exit_no_check

    return ret


def create_config_dir():
    """
    Create config dir

    return:
        0 ok, 1 else
    """
    file_does_exist = 0
    ret = EXIT_SUCCESS
    if check_config_dir() > file_does_exist:
        try:
            print("Create {}".format(BLACKARCH_CONFIG))
            err = subprocess.run(['mkdir', '-p', BLACKARCH_CONFIG],
                                 stderr=subpress.PIPE)
        except:
            print("Could not create {}".format(BLACKARCH_CONFIG))
            print(err.stderr.decode('utf-8'))
            ret = EXIT_FAILURE

    return ret


def get_pkgbuild_files():
    """
    Clone Blackarch Repo

    return:
        0 if cloning was successful, 1 else
    """
    ret = EXIT_SUCCESS
    try:
        err = subprocess.run(['git', 'clone', BLACKARCH_REPO, LOCAL_REPO],
                             stderr=subprocess.PIPE)
    except:
        print("Could not clone {}".format(BLACKARCH_REPO))
        print(err.stderr.decode('utf-8'))
        ret = EXIT_FAILURE
    return ret


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


def write_to_config(name, value):
    """
    Save variables to config file

    Arguments:
        name(str) - name of option
        value(str) - write value to config file
    """
    ret = EXIT_SUCCESS
    try:
        with ope?!?jedi=3, n(BLACKARCH_CONFIG, 'w+'):?!? (*_*param value*_*, param ..., param sep, param end, param file, param flush) ?!?jedi?!?' '
            print("write {} to {} here".format(value, BLACKARCH_CONFIG))
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
    if args['default']:
        write_to_config('repo_path', args['default'])



def main():
    """
    main function of blackman
    """
    create_config_dir()
    args = parse_arguments()
    handle_args(args)


if __name__ == "__main__":
    main()
