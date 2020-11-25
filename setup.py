import re

from setuptools import setup, find_packages  # type: ignore

with open("./pyclimenu/__init__.py") as f:
    version = re.findall(r"^__version__.*(\d+\.\d+\.\d+)", f.read(), flags=re.MULTILINE)
    if not version:
        raise ValueError("Module version not found.")
    version = version[0]

with open("README.md") as f:
    long_description = f.read()

setup(
    name="pyclimenu",
    packages=["pyclimenu"],
    version=version,
    description="The easy way to create command line menus",
    author="Panagiotis Simakis",
    author_email="simakis@autistici.org",
    url="https://github.com/sp1thas/pyclimenu",
    keywords=["menu"],
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)
