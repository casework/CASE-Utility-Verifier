#'Approved for Public Release; Distribution Unlimited. Case Number 18-1041'.


# NOTICE
# 
# This software was produced for the U.S. Government under
# contract SB-1341-14-CQ-0010, and is subject to the Rights
# in Data-General Clause 52.227-14, Alt. IV (DEC 2007)
#
# (c) 2018 The MITRE Corporation. All Rights Reserved.


#====================================================
from setuptools import setup

setup(
    name='case',
    version='0.1.0',
    description='Defines an API for CASE.',
    long_description=(
        'This is a low-level API for the CASE/UCO ontology used to *generate* RDF graphs.'),
    install_requires=[
        'rdflib',
        'rdflib-jsonld'
    ],
    py_modules=['case'],
)
