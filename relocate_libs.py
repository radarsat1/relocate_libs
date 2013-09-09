#!/usr/bin/env python

import sys, os
import subprocess

if len(sys.argv) < 3:
    print """
This tool calls "install_name_tool -change" for each library or
executable, replacing the specified string in any matched library
names.  It can be used for example to change library linkage to
@executable_path/../Resources... when creating an app bundle.

Usage: relocate_libs <from-string> <to-string> <libanything.dylib ..>

Example: relocate_libs /usr/local/lib @executable_path/../Resources/lib *.dylib
"""
    sys.exit(0)

FROM = sys.argv[1]
TO = sys.argv[2]

print "Changing `%s' to `%s'"%(FROM, TO)

for lib in sys.argv[3:]:

    haslibs = subprocess.check_output(['otool', '-L', lib]).split('\n')
    if haslibs[0].split(':')[0] != lib:
        print "Unexpected library name, `%s'"%haslibs[0].split(':')[0]
        sys.exit(1)

    haslibs = [x.strip().split()[0] for x in haslibs[1:-1]]

    printed = False
    for hl in haslibs:
        if FROM in hl:
            if not printed:
                print lib
                printed = True
            idx = hl.find(FROM)
            newlib = TO + hl[idx + len(FROM):]
            print "  `%s' -> `%s'"%(hl, newlib)
            print subprocess.check_output(["install_name_tool", "-change",
                                           hl, newlib, lib]).strip()
