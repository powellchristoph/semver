from __future__ import with_statement

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import semver 

classifiers = [
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
]

with open("README", "r") as fp:
    long_description = fp.read()

setup(name="semver",
      version=semver.__version__,
      author="Christopher Powell",
      author_email="powellchristoph@gmail.com",
      py_modules=["semver"],
      description="A Python library that will compare two semantic version strings.",
      long_description=long_description,
      license="MIT",
      classifiers=classifiers
      )
