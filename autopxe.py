#! /usr/bin/env python

from __future__ import print_function
import argparse

import parsers
from utils import *
import utils
from sitedep import *

_mountpoint = SiteDep["dirs"]["mountpoint"]

def parse_args():
    parser = argparse.ArgumentParser(
            description="Add a new ISO to your PXE server!")
    parser.add_argument('iso_file', type=str,
                        help="The ISO file to be added")
    parser.add_argument('-v', '--verbose', action="store_true")
    parser.add_argument('--dryrun', action="store_true")
    return parser.parse_args()

def mount_iso(path):
    if not os.path.isdir(_mountpoint):
        os.system("mkdir %s" % _mountpoint)
    os.system("mount %s %s" % (path, _mountpoint))

def extract_files(file_parser):
    tags = file_parser.parse()
    print("Distro:         " + tags[file_parser.DISTRO])
    print("Version:        " + tags[file_parser.VERSION])
    print("Type:           " + tags[file_parser.TYPE])
    print("Architecture:   " + tags[file_parser.ARCH])

    vprint("Init files:     " + str(file_parser.get_init_files()))
    vprint("Init directory: " + str(file_parser.get_init_directory()))

    # Create destination directory
    dest = SiteDep["dirs"]["plugins"] + "/" + file_parser.get_init_directory()
    utils.dryrun(os.system, "mkdir -p \"%s\"" % os.path.normpath(dest))

    # Copy init files
    for init_file in file_parser.get_init_files():
        filepath = _mountpoint + "/"+ init_file
        utils.dryrun(os.system, "cp --no-clobber %s %s" % tuple(map(os.path.normpath, (filepath, dest))))

def copy_extras(file_parser):
    # Create destination directory
    dest = SiteDep["dirs"]["shares"] + "/" + file_parser.get_shares_directory()
    utils.dryrun(os.system, "mkdir -p \"%s\"" % os.path.normpath(dest))

    # Copy share files
    for share_file in file_parser.get_share_files():
        filepath = _mountpoint + "/"+ share_file
        utils.dryrun(os.system, "cp --no-clobber %s %s" % tuple(map(os.path.normpath, (filepath, dest))))

def unmount_iso():
    os.system("umount %s" % _mountpoint)

def main():
    print("AUTOPXE: http://github.com/Peaches491/autopxe")
    args = parse_args()

    # Set verbosity
    utils._VERBOSE = args.verbose
    vprint("Verbose printing enabled")
    utils._DRYRUN = args.dryrun
    if utils._DRYRUN:
        print("Executing Dry Run (no files will be changed)")

    iso_file = args.iso_file
    file_parser = parsers.select_parser(iso_file)

    mount_iso(iso_file)
    extract_files(file_parser)
    copy_extras(file_parser)
    # unmount_iso()

if __name__ == "__main__":
    main()

