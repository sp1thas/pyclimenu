import re

from setuptools import setup, find_packages  # type: ignore

with open("./pyclimenu/__init__.py") as f:
    version = re.findall(r"^__version__.*(\d+\.\d+\.\d+)", f.read(), flags=re.MULTILINE)
    if not version:
        raise ValueError("Module version not found.")
    version = version[0]

setup(
    name="pyclimenu",
    packages=find_packages(),
    version=version,
    description="The easy way to create command line menus",
    author="Panagiotis Simakis",
    author_email="simakis@autistici.org",
    url="https://github.com/sp1thas/pyclimenu",
    download_url="https://github.com/sp1thas/pyclimenu/archive/master.zip",
    keywords=["menu"],
    include_package_data=True,
    classifiers=[],
    zip_safe=False,
)
