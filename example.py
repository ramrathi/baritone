from __future__ import absolute_import
from __future__ import print_function
import os
import logging
import warnings
warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    dburl = 'sqlite:///new.db'
    djv = Dejavu(dburl=dburl)
    # Fingerprint all the mp3's in the directory we give it
    djv.fingerprint_directory("mp3", [".mp3"])
    # Or use a recognizer without the shortcut, in anyway you would like
    recognizer = FileRecognizer(djv)
    song = recognizer.recognize_file(
        "hello.mp3"
    )
    print((song))
