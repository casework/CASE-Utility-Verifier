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
    name='case-python-api',
    version='0.1.0',
    description='CASE/UCO API for creating RDF graphs and verifying ontological compliance.',
    long_description=(
        'The Natural Language Glossary (NLG.py) has the necessary checks for ensuring proper inheritance, vocabulary, required parameters, and types; calling its functions (which return RDF nodes via case.py) is the typical way to use the API. However, in rare circumstances where CASE compliance is not desired case.py functions can be explicitly called to create RDF nodes.'),
    install_requires=[
        'rdflib',
        'rdflib-jsonld'
    ],
    py_modules=['case',
                'NLG'],
)
