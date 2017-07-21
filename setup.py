import os
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as fo:
    long_description = fo.read()


setup(
    name='case',
    version='0.0.1',
    description='Defines an API for CASE.',
    long_description=long_description,
    install_requires=[
        'rdflib',
        'rdflib-jsonld'
    ]
)