# Standard Python Libraries
import codecs
from glob import glob
from os.path import abspath, basename, dirname, join, splitext

# Third-Party Libraries
from setuptools import find_packages, setup


# Below two methods were pulled from:
# https://packaging.python.org/guides/single-sourcing-package-version/
def read(rel_path):
    """Open a file for reading from a given relative path."""
    here = abspath(dirname(__file__))
    with codecs.open(join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(version_file):
    """Extract a version number from the given file path."""
    for line in read(version_file).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setup(
    name="timelapse-pi",
    version=get_version("src/_version.py"),
    description=" A python module to turn a Raspberry Pi into a Timelapse camera node. ",
    long_description=open("README.md").read(),
    url="https://github.com/bjb28/timelapse-pi",
    license="License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
    author="Bryce Beuerlein",
    author_email="swarvingprogrammer@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires=">=3.7.7",
    package_dir={"": "src"},
    packages=find_packages("src"),
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    install_requires=[

    ],
    extras_require={
        "dev": [
            "black >= 20.8b1",
            "coverage",
            "coveralls != 1.11.0",
            "flake8 >= 3.8.4",
            "pytest",
            "pytest-cov",
            "ipython >= 7.0",
        ],
        "prod": [
            "picamera",
        ]
    },
    # TODO Add entry points.
)
