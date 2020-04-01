import sys
import os
import pathlib
import requests 
import pycurl
from io import BytesIO 
import urllib.request
from progress.bar import Bar
from progress.spinner import Spinner
import tarfile
import zipfile

DIR = str(pathlib.Path(__file__).parent.absolute().parent.absolute())

class Getter:
    def get(self, url, to):
        self.p = None

        def update(blocks, bs, size):
            if not self.p:
                self.p = Bar(to, max=size)
            else:
                if size < 0:
                    self.p.update()
                else:
                    self.p.goto(blocks * bs)

        urllib.request.urlretrieve(url,DIR+'/pretrained.tar.gz',update)
        self.p.finish()

def download_model(src):
	if os.path.isfile(DIR+'/pretrained.tar.gz'):
		return ("File already present",True)
	# curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.6.1/deepspeech-0.6.1-models.tar.gz
	# tar xvf deepspeech-0.6.1-models.tar.gz
	# response = StringIO.StringIO()
	url = 'https://github.com/mozilla/DeepSpeech/archive/v0.6.1.tar.gz'
	print("Starting Download!")
	# data = urllib.request.urlretrieve(url,DIR+'/pretrained.tar.gz')
	Getter().get("https://github.com/mozilla/DeepSpeech/archive/v0.6.1.tar.gz",DIR+'/pretrained.tar.gz' )
	print("Finished Download")
	# print(data)
	base_name = os.path.basename(url)
	file_name, file_extension = os.path.splitext(base_name)

def extract_file(path, to_directory='.'):
    if path.endswith('.zip'):
        opener, mode = zipfile.ZipFile, 'r'
    elif path.endswith('.tar.gz') or path.endswith('.tgz'):
        opener, mode = tarfile.open, 'r:gz'
    elif path.endswith('.tar.bz2') or path.endswith('.tbz'):
        opener, mode = tarfile.open, 'r:bz2'
    else: 
        return (("Could not extract `%s` as no appropriate extractor is found") % path,False)

    cwd = os.getcwd()
    os.chdir(to_directory)

    try:
        file = opener(path, mode)
        try: file.extractall()
        finally: file.close()
    finally:
        os.chdir(cwd)
# def load_data():
#     if not os.path.exists(DATA_DIR):
#         download_data()
#     data = read_data_from_disk(DATA_DIR)
#     return data

download_model(123)
extract_file(DIR+'/pretrained.tar.gz',DIR)