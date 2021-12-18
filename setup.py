from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'requirements.txt')) as f:
    requirements = [r.rstrip().split('#')[0].rstrip() for r in f]


setup(
    name = 'pipeline',
    version='0.0.1a',
    description="Seahawks Pipeline",
    long_description="Pipeline Project with Raphael",
    author='David Godinez',
    packages = find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=requirements
)