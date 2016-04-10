from __future__ import print_function
_VERBOSE = False
_DRYRUN = False

_VERBOSE_LEADER = "(V) "

def dryrun(cmd, *args, **kwargs):
    if _DRYRUN:
        print("DRYRUN: ", end="")
    print(str(cmd.__module__) + '.' + str(cmd.__name__) + str(args) + str(kwargs))
    if not _DRYRUN:
        cmd(*args, **kwargs)

def vprint(*args, **kwargs):
    global VERBOSE
    if _VERBOSE:
        string = str(*args)
        lines = string.splitlines(True)
        if len(lines) == 1:
            string = _VERBOSE_LEADER + string
        else:
            string = _VERBOSE_LEADER.join(string.splitlines(True))
        print(string, **kwargs)
