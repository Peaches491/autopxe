from collections import OrderedDict
from utils import *
from sitedep import *

import os

class BaseParser():
    DISTRO =  "distro"
    VERSION = "version"
    TYPE =    "type"
    ARCH =    "arch"

    def __init__(self, filename):
        self._isopath = filename

    def parse(self, filename):
        return {}

    def get_filename(self, strip_extension=False):
        filename = os.path.basename(self._isopath)
        if strip_extension:
            filename = os.path.splitext(filename)[0]
        return filename

    def get_distro(self):
        distro = self.get_filename().split("-")[0]
        return distro

    def get_init_files(self):
        return SiteDep[self.get_distro()]["init_files"]

    def get_share_files(self):
        return SiteDep[self.get_distro()]["share_files"]

    def get_init_directory(self, absolute=False):
        path = ""
        if absolute:
            path += SiteDep["plugins"]

        tags = self.parse()
        distro = self.get_distro()
        path += tags[self.DISTRO] + "/"
        path += tags[self.VERSION] + "/"
        path += tags[self.TYPE] + "/"
        path += tags[self.ARCH] + "/"
        return path

    def get_shares_directory(self, absolute=False):
        path = ""
        if absolute:
            path += SiteDep["shares"]

        tags = self.parse()
        distro = self.get_distro()
        path += tags[self.DISTRO] + "/"
        path += tags[self.VERSION] + "/"
        path += tags[self.TYPE] + "/"
        path += tags[self.ARCH] + "/"
        return path
