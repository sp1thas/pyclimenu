from distutils.core import setup

def readme():
    with open('README.rst') as f:
        return f.read()
setup(
  name = 'pyclimenu',
  packages = ['pyclimenu'],
  version = '0.1.1.9',
  description = 'The easy way to create command line menus',
  author = 'Panagiotis Simakis',
  author_email = 'simakis@autistici.org',
  url = 'https://github.com/sp1thas/pyclimenu',
  download_url = 'https://github.com/sp1thas/pyclimenu/archive/master.zip',
  keywords = ['menu'],
  include_package_data=True,
  classifiers = [],
  zip_safe=False,
  long_description=readme()
)
