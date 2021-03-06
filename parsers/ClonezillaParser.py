from collections import OrderedDict

from .BaseParser import BaseParser

class ClonezillaParser(BaseParser):

    def __init__(self, filename):
        BaseParser.__init__(self, filename)

    def parse(self):
        fields = self.get_filename(strip_extension=True).split("-")
        fields.reverse()

        tags = OrderedDict()
        tags[self.DISTRO] = self.get_distro()
        fields.pop() # Remove the distro
        fields.pop() # Remove the 'live'

        if len(fields) >= 3:
            tags[self.VERSION] = "-".join([fields.pop(), fields.pop()])
        else:
            tags[self.VERSION] = fields.pop()
        tags[self.TYPE] = fields.pop()
        tags[self.ARCH] = fields.pop()

        return tags

