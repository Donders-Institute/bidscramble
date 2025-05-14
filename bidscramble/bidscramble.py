#!/usr/bin/env python3
r"""
 __              __       __         __       __
|  | >  __| |<< |<< |<<  |  | |\ /| |  | |   |
|<>' | |<<| --  |   |>>| |><| | < | |<>' |   |<<
|__' | |__| >>| |__ |  \ |  | |   | |__' |<< |__

BIDScramble is a powerful tool that generates scrambled or pseudo-random BIDS datasets from existing
BIDS-structured data. It carefully preserves the statistical distributions of user-specified variables
while maintaining the effects of interest, ensuring that the synthetic data remains analytically useful.
Crucially, the output contains no or minimal indirect personal data, making it privacy-compliant and
untraceable to original subjects.

This tool enables researchers to safely explore, prototype, and test their analysis pipelines on
realistic yet anonymized data. Since the scrambled datasets retain key statistical properties, pipelines
should behave similarly to how they would on real data — accelerating development without compromising
privacy.

Explore the full documentation on Read the Docs: https://bidscramble.readthedocs.io
"""

import argparse
import textwrap
import sys
from bidscramble import check_version, console_scripts, __version__


def main():
    """Console script entry point"""

    _, _, versionmessage = check_version()

    parser = argparse.ArgumentParser(prog='bidscramble',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=textwrap.dedent(__doc__),
                                     epilog='examples:\n'
                                            '  bidscramble -l\n ')
    parser.add_argument('-l', '--list',    help='List all executables (i.e. the apps, bidsapps and utilities)', action='store_true')
    parser.add_argument('-v', '--version', help='Show the installed version and check for updates', action='version', version=f"BIDScramble-version:\t{__version__}, {versionmessage}")

    # Parse the input arguments and run bidscramble(args)
    args = parser.parse_args(None if sys.argv[1:] else ['--help'])

    console_scripts(show=args.list)


if __name__ == "__main__":
    main()
