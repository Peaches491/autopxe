import unittest
import parsers

ubuntu_test_paths = {
    "/media/Storage/ISOs/Ubuntu/xenial/ubuntu-16.04-beta2-server-amd64.iso": {
        parsers.BaseParser.DISTRO:       "ubuntu",
        parsers.BaseParser.VERSION:      "16.04-beta2",
        parsers.BaseParser.TYPE:         "server",
        parsers.BaseParser.ARCH:         "amd64",
    },
    "/media/Storage/ISOs/Ubuntu/xenial/ubuntu-16.04-server-amd64.iso": {
        parsers.BaseParser.DISTRO:       "ubuntu",
        parsers.BaseParser.VERSION:      "16.04",
        parsers.BaseParser.TYPE:         "server",
        parsers.BaseParser.ARCH:         "amd64",
    },
}

tag_list = [
    parsers.BaseParser.DISTRO,
    parsers.BaseParser.VERSION,
    parsers.BaseParser.TYPE,
    parsers.BaseParser.ARCH,
]


class TestParsers(unittest.TestCase):

    def test_test(self):
        for path, given_tags in ubuntu_test_paths.iteritems():
            for tag in tag_list:
                file_parser = parsers.select_parser(path)
                tags = file_parser.parse()
                self.assertEqual(tags[tag], given_tags[tag])

