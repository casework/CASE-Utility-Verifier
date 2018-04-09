### CASE API
This repository will serve as a PoC of Digital Forensic tool mappings.
The CASE-API wraps [RDFLib](https://rdflib.readthedocs.io/en/stable/) for a JSON-LD
schematic. 


#### Quickstart
1.``` python setup.py install```


#### src
This directory contains all source files for the CASE-API.
* **case.py**:  Original PoC API implementation of the ontology on [github](www.github.com/caseworks/case). 
APIs for various tools will likely inherent from classes within this script.
* **case-example.py** : Example implementation of CASE/UCO as defined on the public facing github.



#### Unittests
This directory contains all unit test files for the Python
CASE-API. The unittest module is being used for all Python testing within this repo.

##### Running Unittests
```
python unittest.test
```
