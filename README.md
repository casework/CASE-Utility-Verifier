# Cyber-investigation Analysis Standard Expression (CASE)

_Read the [CASE Wiki tab](https://github.com/casework/CASE/wiki) to learn **everything** you need to know about the Cyber-investigation Analysis Standard Expression (CASE) ontology._
_For learning about the Unified Cyber Ontology, CASE's parent, see [UCO](https://github.com/ucoProject/UCO)._

# CASE Python API

### Development Status: Alpha

Alpha status implies:
- Designation of versions of CASE and UCO the project supports.
- Follow Semantic Versioning (SEMVER).

### Quickstart

1. ``` python setup.py install```
2. Import `case.py` and `NLG.py` into the file you plan to implement CASE.


### NLG.py & CASE.py

The Natural Language Glossary (NLG) is an alphabetical list of types of CASE classes (categories of CASE types).
The functions in `NLG.py` create CASE objects (instances of such types) while automatically checking ontology and type.
The API (`case.py`) could be used directly to create non-typed objects if ontology and type checking are not requirements.
However, we advise against this to maintain consistency across community usage of the ontology.


Note that different versions of the NLG exist for different realizations of the Unified Cyber Ontology.
The human legible NLG corresponding to this version of CASE (one realization of UCO) can be found here:
https://casework.github.io/case/case-v0.1.0-natural-language-glossary.html


The API wraps [RDFLib](https://rdflib.readthedocs.io/en/stable/) for a JSON-LD
schematic. This verison is only directly adoptable via Python but JSON-LD is also supported in Javascript, PHP, Ruby, Java, C#, and Go.


### Examples

The `example` folder contains a slimmed down NLG, for an understanding of some of the basic function variations that exist, as well as a template for all types of conditions checked by the NLG functions.

# NLG Autogeneration (only for CASE team to manage API)

*Note that currently the script will not function properly because v0.1.0 of CASE does not have a cardinality field for each object and property. When this is added the script will be stable and new_NLG.py in the outputs folder will not have missing body checks.*

Dependency: [Ontospy](https://github.com/casework/Ontospy)

When CASE's base specification (Turtle files) changes this script can be used to automatically regenerate the NLG.py functions for the next release. Therefore, this should only be run by the CASE team - eventually it will move to a new (possibly backend) repo where a CI/CD framework is placed.

To run Ontospy must be installed, and the Turtle files combined into one.
Then run ```python autogen-api.py <path-to-turtle-file>```.
(Note there is a ToDo list in the `autogen-api.py` file so that it can align with changes that may occur in the API, as well as other add new features such as better CLI flags, a CSV export of all object names and properties for the Ontologists and Mappers teams to use for quick reference, etc.)

# I have a question!

Before you post a Github issue or send an email ensure you've done this checklist:

1. [Determined scope](https://caseontology.org/ontology/start.html#scope) of your task. It is not necessary for most parties to understand all aspects of the ontology, mapping methods, and supporting tools.

2. Familiarize yourself with the [labels](https://github.com/casework/CASE-API-Python/labels) and search the [Issues tab](https://github.com/casework/CASE-API-Python/issues). Typically, only light-blue and red labels should be used by non-admin Github users while the others should be used by CASE Github admins.
*All but the red `Project` labels are found in every [`casework`](https://github.com/casework) repository.*
