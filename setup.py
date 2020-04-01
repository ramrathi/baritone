import os
from setuptools import setup

'''
Just a silly little library I made to make state of the art voice to text
easy to use by just importing and running.

'''

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "baritone",
    version = "0.0.1",
    author = "Ram Rathi",
    author_email = "ryrathi@gmail.com",
    description = ("A ready-to-use, voice to text, wrapper library based on a pretrained version of Mozilla and Baidu's DeepSpeech architecture"),
    license = "MIT",
    keywords = "example documentation tutorial",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['an_example_pypi_project', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 1- Planning",
        "Topic :: Utilities",
    ],
    install_requires=[            
          'youtube-dl',
          'deepspeech',
      ],
)