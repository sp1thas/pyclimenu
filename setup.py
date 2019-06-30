from pyclimenu import __version__
from distutils.core import setup

setup(
  name='pyclimenu',
  packages=['pyclimenu'],
  version=__version__,
  description='The easy way to create command line menus',
  author='Panagiotis Simakis',
  author_email='simakis@autistici.org',
  url='https://github.com/sp1thas/pyclimenu',
  download_url='https://github.com/sp1thas/pyclimenu/archive/master.zip',
  keywords=['menu'],
  include_package_data=True,
  classifiers=[],
  zip_safe=False,
)
