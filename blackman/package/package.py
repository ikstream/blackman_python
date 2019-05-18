'''
Package class for blackman
'''

import re
import subprocess

def is_in_blackarch_repo(pkg):
    '''
    Check if a package is in the blackarch repo

    Arguments:
        pkg(str) - Package to check

    Return:
        (bool) True if in BlackArch, else False
    '''
    output = subprocess.getoutput('pacman -Ss ' + pkg).split('/')
    if output[0] == 'blackarch':
        return True

    return False


class Package():
    '''
    Package class provides information and functions per package
    '''
    def __init__(self, name):
        self.__make_depends = list()
        self.__depends = list()
        self.__installed_version = 0
        self.__name = name
        self.__path = ''


    def set_path(self, path):
        '''
        set path to PKGBUILD file

        Arguments:
            path(str) - path to PKGBUILD file
        '''
        self.__path = path


    def collect_makedepends(self):
        '''
        collect makedepends from PKGBUILD file
        '''
        m_d = re.compile('^makedpends')
        with open(self.__path, 'r') as pkg_build:
            for line in pkg_build:
                if m_d.match(line):
                    line = line[12:].strip()
                    while not line.endswith(")\n"):
                        for dep in line.strip().split():
                            self.__make_depends.append(re.sub(r'\'', '', dep))

                        line = next(pkg_build)

                    for dep in line[:-2].strip().split():
                        self.__make_depends.append(re.sub(r'\'', '', dep))


    def get_deps_to_build(self):
        '''
        Return all dependencies that need to be build

        Return:
            build_deps(list) - list of dependencies to build
        '''
        build_deps = list()
        for pkg in self.__make_depends:
            if is_in_blackarch_repo(pkg):
                build_deps.append(pkg)

        for pkg in self.__depends:
            if is_in_blackarch_repo(pkg):
                build_deps.append(pkg)

        return build_deps


    def get_deps_to_install(self):
        '''
        Return all dependecies that can are in the official repo

        Return:
            inst_deps(list) - list of dependecies to install
        '''
        inst_deps = list()
        for pkg in self.__make_depends:
            if not is_in_blackarch_repo(pkg):
                inst_deps.append(pkg)

        for pkg in self.__depends:
            if not is_in_blackarch_repo(pkg):
                inst_deps.append(pkg)

        return inst_deps
