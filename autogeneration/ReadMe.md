## NLG.py Regeneration

*Note that currently the script will not function properly because v0.1.0 of CASE does not have a cardinality field for each object and property. When this is added the script will be stable.*

When CASE's base specification (Turtle files) changes this script can be used to automatically regenerate the NLG.py functions for the next release. Therefore, this should only be run by the CASE team - eventually it will move to a new (possibly backend) repo where a CI/CD framework is placed.

To run Ontospy must be installed, and the Turtle files combined into one.
Then run ```python autogen-api.py <path-to-turtle-file>```.
(Note there is a ToDo list in the `autogen-api.py` file so that it can align with changes that may occur in the API, as well as other add new features such as better CLI flags, a CSV export of all object names and properties for the Ontologists and Mapperse teams to use for quick reference, etc.)