"""
Package setup script for Mediator, Profuder’s rebranded popular TV API.

This script uses setuptools to define the package metadata, including the name, version, description, and dependencies.
The metadata is read from the `__init__.py` file, while the long description is read from the `README.md` file. The
dependencies are read from the `requirements.txt` file.

To build and distribute the package, run:

    $ python setup.py sdist bdist_wheel
    $ twine upload dist/*

This will create a source distribution and a wheel distribution in the `dist` directory, and upload them to the PyPI
repository using twine.

To install the package and its dependencies, run:

    $ pip install mediator

This will download and install the package from the PyPI repository, along with its dependencies specified in the
`requirements.txt` file.

To install the package for development and testing, run:

    $ pip install -e .[dev]

This will install the package in editable mode, along with the development and testing dependencies specified in the
`extras_require` field of the setup() call.

For more information on how to use and contribute to the package, see the project repository at
https://github.com/bastiensoucasse/mediator.
"""

from typing import Dict

from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

about: Dict[str, str] = {}
with open("mediator/__init__.py", encoding="utf-8") as f:
    exec(f.read(), about)

setup(
    name=about["__project__"],
    version=about["__version__"],
    description=about["__doc__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__email__"],
    maintainer=about["__maintainer__"],
    maintainer_email=about["__maintainer_email__"],
    url=about["__url__"],
    packages=find_packages(),
    install_requires=requirements,
    extra_requires={"dev": ["black", "pylint"]},
)
