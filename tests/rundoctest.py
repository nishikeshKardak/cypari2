#!/usr/bin/env python

import os
import sys
import cypari2
import doctest

path = os.path.dirname(__file__)
if path:
    os.chdir(path)

failed = 0
attempted = 0
for mod in [cypari2.closure, cypari2.convert, cypari2.gen,
            cypari2.handle_error, cypari2.pari_instance, cypari2.stack,
            cypari2.string_utils]:

    print("="*80)
    print("Testing {}".format(mod.__name__))
    test = doctest.testmod(mod, optionflags=doctest.ELLIPSIS|doctest.REPORT_NDIFF|doctest.IGNORE_EXCEPTION_DETAIL)
    failed += test.failed
    attempted += test.attempted

print("="*80)
print("Summary result for cypari2:")
print("   attempted = {}".format(attempted))
print("   failed = {}".format(failed))

sys.exit(failed)
