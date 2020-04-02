#!/usr/bin/python

import os
import sys
import warnings
import argparse

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer
from dejavu.recognize import MicrophoneRecognizer
from dejavu.version import __version__
from argparse import RawTextHelpFormatter

warnings.filterwarnings("ignore")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Dejavu: Audio Fingerprinting library",
        formatter_class=RawTextHelpFormatter
    )
    parser.add_argument(
        '-d',
        '--dburl',
        nargs='?',
        default=None,
        help='Database URL to use. As supported by SQLAlchemy (RFC-1738). '
             'Will read $DATABASE_URL env var if not specified\n'
        'Usages: \n'
        '--dburl mysql://user:pass@localhost/database\n'
    )
    parser.add_argument(
        '-f',
        '--fingerprint',
        nargs='*',
        help='Fingerprint files in a directory\n'
        'Usages: \n'
        '--fingerprint /path/to/directory extension\n'
        '--fingerprint /path/to/directory'
    )
    parser.add_argument(
        '-r',
        '--recognize',
        nargs=2,
        help='Recognize what is playing through the microphone\n'
        'Usage: \n'
        '--recognize mic number_of_seconds \n'
        '--recognize file path/to/file \n'
    )
    parser.add_argument(
        '-l',
        '--limit',
        nargs='?',
        default=None,
        help='Number of seconds from the start of the music files to limit fingerprinting to.\n'
        'Usage: \n'
        '--limit number_of_seconds \n'
    )
    parser.add_argument(
        '--version',
        action='version',
        version=__version__
    )

    args = parser.parse_args()

    if not args.dburl:
        # args.dburl = os.environ['DATABASE_URL']
        args.dburl = 'new.db'
        print(args.dburl)

    if not args.fingerprint and not args.recognize:
        parser.print_help()
        sys.exit(0)

    djv = Dejavu(dburl=args.dburl, fingerprint_limit=args.limit)
    if args.fingerprint:
        # Fingerprint all files in a directory
        if len(args.fingerprint) == 2:
            directory = args.fingerprint[0]
            extension = args.fingerprint[1]
            print(
                "Fingerprinting all .%s files in the %s directory" %
                (extension, directory)
            )
            djv.fingerprint_directory(directory, ["." + extension], 4)

        elif len(args.fingerprint) == 1:
            filepath = args.fingerprint[0]
            if os.path.isdir(filepath):
                print(
                    "Please specify an extension if you'd like to fingerprint a directory!"
                )
                sys.exit(1)
            djv.fingerprint_file(filepath)

    elif args.recognize:
        # Recognize audio source
        song = None
        source = args.recognize[0]
        opt_arg = args.recognize[1]

        if source in ('mic', 'microphone'):
            song = djv.recognize(MicrophoneRecognizer, seconds=opt_arg)
        elif source == 'file':
            song = djv.recognize(FileRecognizer, opt_arg)
        print(song)

    sys.exit(0)
