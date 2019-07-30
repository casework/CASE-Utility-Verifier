# CASE NLG VERIFIER v0.1.0

"""
The Natural Language Glossary (NLG) is an alphabetical list of types of CASE classes (categories of CASE types).
The functions in this file create CASE objects (instances of such types) while automatically checking ontology and type.
The API (case.py) could be used directly to create non-typed objects if ontology and type checking are not requirements.
However, we advise against this to maintain consistency across community usage of the ontology.

Note that different versions of the NLG exist for different realizations of the Unified Cyber Ontology.
The human legible NLG corresponding to this version of CASE (one realization of UCO) can be found here:
https://casework.github.io/case/case-v0.1.0-natural-language-glossary.html

-----------------------------------------------------
NOTES ON FUNCTION STRUCTURE

    CASE objects:         Search "CREATE A CASE OBJECT" in the API (case.py) to understand the high-level CASE objects.
    Parameters:           All parameters use underscores coming in and are set by default to a Missing object.
    Required parameters:  The CASE Document class is passed in ('_sub' functions also require their superseding CASE class).
    Ontology parameters:  All other parameters are specified by the CASE ontology, and may be required or optional.
    Function docstrings:  'Any number of' = must be a list (otherwise pass in a single Python object)
                          'Exactly one' or 'At least one' = required parameter
                          'At most one' = optional parameter
    Body asserts:         1) superseding CASE class/type (if applicable)
                          2) required parameters
                          3) optional parameters 
    Return:               The desired object is instantiated and parameters converted to CamelCase for JSON-LD output.

    See examples/NLG_template.txt for a list of all instances of function definitions, docstrings, and assert statements found in the NLG.

-----------------------------------------------------
ORGANIZATION FOR DEVELOPERS

As development of the ontology moves forward new functions and API classes may be added.
If you wish to contribute to improvement, follow these note-taking standards to help us stay on the same proverbial page.
    - #TODO:NothingElseToCheck - If no parameters are checked (incomplete ontology or ambiguity).
    - #NOCHECK:<param_name>    - If a parameter does not have a check (but at least one other parameter does).
    - #TODO:<type_name>        - If a standard has not been defined yet for a type check (e.g. #TODO:URI).
                                 Custom functions for such types may be found in the last section of this file.
    - There are two 'Identity' NLG types, one a 'core_' and one a 'propbundle_'.
      In assert output state which is required via "of type Identity (core)" or "of type Identity (propbundle)".
"""


import case
import sys
import unittest
import datetime.datetime

class Missing(object):
    def __init__(self):
        self.is_missing = True


#=====================================================
#-- CORE

def core_Action(case_doc, actionStatus=Missing(), environment=Missing(), error=Missing(), subAction=Missing()):
	'''
