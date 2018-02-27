# CASE/UCO Python API

This is a low-level API for the [CASE/UCO](https://casework.github.io/case) ontology
used to *generate* RDF graphs.
This API is designed to be a thin wrapper around the rdflib library used to create
RDF graphs. The rdflib library can then be used to inject and read already
created graphs.

*NOTE: This API currently does not perform any validation and therefore requires the
user to know how to properly structure CASE/UCO elements.*

## Install
```
git clone https://github.com/casework/case-api-python.git
pip install case-api-python
```


## Usage
Below is an example of using the case API to generate a json-ld file.

```python
import case
import datetime


document = case.Document()

instrument = document.create_uco_object(
    'Tool',
    name='Super Forensic Tool 3000',
    version='3.4.5',
    toolType='Extraction',
    creator='Frank Grimes')

performer = document.create_uco_object('Identity')
performer.create_property_bundle(
    'SimpleName',
    givenName='John',
    familyName='Doe')

action = document.create_uco_object(
    'ForensicAction',
    startTime=datetime.datetime(2017, 7, 21, 13, 32),
    endTime=datetime.datetime(2017, 7, 21, 14, 12))
action.create_property_bundle(
    'ActionReferences',
    performer=performer,
    instrument=instrument,
    # object and result should be filled with
    # input and output uco objects for this Forensic action.
    object=None,
    result=[])

document.serialize(format='json-ld', destination='output.json')
```

output.json :
```json
{
  "@context": {
    "@vocab": "http://case.example.org/core#",
    "case": "http://case.example.org/core#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@graph": [
    {
      "@id": "_:15249350-6615-48b4-b332-c983dc16af7e",
      "@type": "ActionReferences",
      "instrument": {
        "@id": "f0a52e1f-d90a-4e60-8f66-b01c1e73051c"
      },
      "performer": {
        "@id": "e706a541-3ca0-486a-ab47-e30ef983ad9d"
      }
    },
    {
      "@id": "f0a52e1f-d90a-4e60-8f66-b01c1e73051c",
      "@type": "Tool",
      "createdTime": {
        "@type": "xsd:dateTime",
        "@value": "2017-07-21T13:43:59.182000"
      },
      "creator": "Frank Grimes",
      "name": "Super Forensic Tool 3000",
      "toolType": "Extraction",
      "version": "3.4.5"
    },
    {
      "@id": "_:469c1da9-403b-4cc9-9d95-de38b0a92ce9",
      "@type": "SimpleName",
      "familyName": "Doe",
      "givenName": "John"
    },
    {
      "@id": "963e9e35-b8b5-4696-a7db-b1681b22e90c",
      "@type": "ForensicAction",
      "createdTime": {
        "@type": "xsd:dateTime",
        "@value": "2017-07-21T13:43:59.183000"
      },
      "endTime": {
        "@type": "xsd:dateTime",
        "@value": "2017-07-21T14:12:00"
      },
      "propertyBundle": {
        "@id": "_:15249350-6615-48b4-b332-c983dc16af7e"
      },
      "startTime": {
        "@type": "xsd:dateTime",
        "@value": "2017-07-21T13:32:00"
      }
    },
    {
      "@id": "e706a541-3ca0-486a-ab47-e30ef983ad9d",
      "@type": "Identity",
      "createdTime": {
        "@type": "xsd:dateTime",
        "@value": "2017-07-21T13:43:59.182000"
      },
      "propertyBundle": {
        "@id": "_:469c1da9-403b-4cc9-9d95-de38b0a92ce9"
      }
    }
  ]
}
```

*(For a more in-depth example, see the [case-implementation-plaso](https://github.com/ucoProject/case-implementation-plaso)
repo which uses this API to export events from a [plaso](https://github.com/log2timeline/plaso) storage file.)*
