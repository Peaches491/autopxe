from .BaseParser import *
from .ClonezillaParser import *
from .UbuntuParser import *

_distro_map = dict()
_distro_map["ubuntu"] = lambda x: UbuntuParser(x)
_distro_map["clonezilla"] = lambda x: ClonezillaParser(x)

def get_distro(filename):
    distro = filename.split("-")[0]
    return distro

def select_parser(input_path):
    filename = os.path.basename(input_path)

    distro = get_distro(filename)
    return _distro_map[distro](input_path)


