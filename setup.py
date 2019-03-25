from distutils.core import setup
from pyclimenu import __version__


readme_file = open('README.md', 'r')
long_description = readme_file.read()
readme_file.close()

setup(
  name = 'pyclimenu',
  packages = ['pyclimenu'],
  version = __version__,
  description = 'The easy way to create command line menus',
  author = 'Panagiotis Simakis',
  author_email = 'simakis@autistici.org',
  url = 'https://github.com/sp1thas/pyclimenu',
  download_url = 'https://github.com/sp1thas/pyclimenu/archive/master.zip',
  keywords = ['menu'],
  classifiers = [],
  long_description=long_description,
  long_description_content_type='text/markdown'
)
