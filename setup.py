from os import path
from distutils.core import setup

here_path = path.abspath(path.dirname(__file__))


with open(path.join(here_path, 'README.rst')) as f:
  long_description = f.read()

setup(
  name = 'pyclimenu',
  packages = ['pyclimenu'],
  version = '0.1.3.3',
  description = 'The easy way to create command line menus',
  author = 'Panagiotis Simakis',
  author_email = 'simakis@autistici.org',
  url = 'https://github.com/sp1thas/pyclimenu',
  download_url = 'https://github.com/sp1thas/pyclimenu/archive/master.zip',
  keywords = ['menu', 'command-line'],
  classifiers = [],
  long_description=long_description,
)
