from setuptools import setup

setup(
    name='case',
    version='0.0.1',
    description='Defines an API for CASE.',
    long_description=(
        'This is a low-level API for the CASE/UCO ontology used to *generate* RDF graphs.'),
    install_requires=[
        'rdflib',
        'rdflib-jsonld'
    ],
    py_modules=['case'],
)