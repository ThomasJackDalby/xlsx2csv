import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "xlsx2csv",
    version = "0.0.1",
    author = "Tom Dalby",
    author_email = "thomasjackdalby@gmail.com",
    description = ("A simple converter for exporting xlsx files to csv without Excel installed."),
    license = "MIT",
    keywords = "xlsx csv converter",
    url = "http://github.com/thomasjackdalby/xlsx2csv",
    packages=['xlsx2csv'],
    scripts=['scripts/xlsx2csv.bat'],
    long_description=read('readme.md'),
)