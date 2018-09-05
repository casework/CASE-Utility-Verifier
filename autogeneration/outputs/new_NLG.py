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
	:return: A CoreCategory object.
	'''




	return case_doc.create_CoreCategory('Action', actionStatus=actionStatus, environment=environment, error=error, subAction=subAction)

def core_Assertion(case_doc):
	'''
	:return: A CoreCategory object.
	'''




	return case_doc.create_CoreCategory('Assertion')

def core_Bundle(case_doc):
	'''
	:return: A CoreCategory object.
	'''




	return case_doc.create_CoreCategory('Bundle')

def core_Identity(case_doc):
	'''
	:return: A CoreCategory object.
	'''




	return case_doc.create_CoreCategory('Identity')

def core_Investigation(case_doc, endAction=Missing(), forensicActions=Missing(), investigator=Missing(), startAction=Missing(), suspectedOffense=Missing(), victim=Missing()):
	'''
	:return: A CoreCategory object.
	'''




	return case_doc.create_CoreCategory('Investigation', endAction=endAction, forensicActions=forensicActions, investigator=investigator, startAction=startAction, suspectedOffense=suspectedOffense, victim=victim)

def core_Location(case_doc):
	'''
	:return: A CoreCategory object.
	'''




	return case_doc.create_CoreCategory('Location')

def core_ProvenanceRecord(case_doc, exhibitNumber=Missing()):
	'''
	:return: A CoreCategory object.
	'''




	return case_doc.create_CoreCategory('ProvenanceRecord', exhibitNumber=exhibitNumber)

def core_Relationship(case_doc, bidirectional=Missing(), kindOfRelationship=Missing(), target=Missing()):
	'''
	:return: A CoreCategory object.
	'''




	return case_doc.create_CoreCategory('Relationship', bidirectional=bidirectional, kindOfRelationship=kindOfRelationship, target=target)

def core_Role(case_doc):
	'''
	:return: A CoreCategory object.
	'''




	return case_doc.create_CoreCategory('Role')

def core_Tool(case_doc, toolType=Missing(), vendor=Missing()):
	'''
	:return: A CoreCategory object.
	'''




	return case_doc.create_CoreCategory('Tool', toolType=toolType, vendor=vendor)

def core_Trace(case_doc):
	'''
	:return: A CoreCategory object.
	'''




	return case_doc.create_CoreCategory('Trace')



#=====================================================
#-- CORE SUB

def core_sub_Annotation(case_doc, parent_object, tag=Missing()):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.CoreCategory) and parent_object.type=='Assertion')),\
	"[core_sub_Annotation] parent_object must be of type Assertion."




	return case_doc.create_SubCategory('Annotation', tag=tag)

def core_sub_BenevolentRole(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.CoreCategory) and parent_object.type=='Role')),\
	"[core_sub_BenevolentRole] parent_object must be of type Role."




	return case_doc.create_SubCategory('BenevolentRole')

def core_sub_ForensicAction(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.CoreCategory) and parent_object.type=='Action')),\
	"[core_sub_ForensicAction] parent_object must be of type Action."




	return case_doc.create_SubCategory('ForensicAction')

def core_sub_MaliciousRole(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.CoreCategory) and parent_object.type=='Role')),\
	"[core_sub_MaliciousRole] parent_object must be of type Role."




	return case_doc.create_SubCategory('MaliciousRole')

def core_sub_NeutralRole(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.CoreCategory) and parent_object.type=='Role')),\
	"[core_sub_NeutralRole] parent_object must be of type Role."




	return case_doc.create_SubCategory('NeutralRole')



#=====================================================
#-- CORE SUB SUB

def core_sub_sub_Attorney(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.CoreCategory) and parent_object.type=='BenevolentRole')),\
	"[core_sub_sub_Attorney] parent_object must be of type BenevolentRole."




	return case_doc.create_SubCategory('Attorney')

def core_sub_sub_Examiner(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.CoreCategory) and parent_object.type=='BenevolentRole')),\
	"[core_sub_sub_Examiner] parent_object must be of type BenevolentRole."




	return case_doc.create_SubCategory('Examiner')

def core_sub_sub_Investigator(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.CoreCategory) and parent_object.type=='BenevolentRole')),\
	"[core_sub_sub_Investigator] parent_object must be of type BenevolentRole."




	return case_doc.create_SubCategory('Investigator')

def core_sub_sub_Subject(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.CoreCategory) and parent_object.type=='MaliciousRole')),\
	"[core_sub_sub_Subject] parent_object must be of type MaliciousRole."




	return case_doc.create_SubCategory('Subject')

def core_sub_sub_Victim(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.CoreCategory) and parent_object.type=='NeutralRole')),\
	"[core_sub_sub_Victim] parent_object must be of type NeutralRole."




	return case_doc.create_SubCategory('Victim')



#=====================================================
#-- DUCK

def duck_Enumeration(case_doc):
	'''
	:return: A DuckCategory object.
	'''




	return case_doc.create_DuckCategory('Enumeration')

def duck_OrderedList(case_doc):
	'''
	:return: A DuckCategory object.
	'''




	return case_doc.create_DuckCategory('OrderedList')

def duck_PropertyBundle(case_doc):
	'''
	:return: A DuckCategory object.
	'''




	return case_doc.create_DuckCategory('PropertyBundle')

def duck_Slot(case_doc):
	'''
	:return: A DuckCategory object.
	'''




	return case_doc.create_DuckCategory('Slot')

def duck_SupportingClasses(case_doc):
	'''
	:return: A DuckCategory object.
	'''




	return case_doc.create_DuckCategory('SupportingClasses')

def duck_UcoObject(case_doc, createdBy=Missing(), propertyBundle=Missing(), specVersion=Missing(), type=Missing()):
	'''
	:return: A DuckCategory object.
	'''




	return case_doc.create_DuckCategory('UcoObject', createdBy=createdBy, propertyBundle=propertyBundle, specVersion=specVersion, type=type)



#=====================================================
#-- DUCK SUB

def duck_sub_AccountType(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_AccountType] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('AccountType')

def duck_sub_ActionStatus(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_ActionStatus] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('ActionStatus')

def duck_sub_ArrayOfAction(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='OrderedList')),\
	"[duck_sub_ArrayOfAction] parent_object must be of type OrderedList."




	return case_doc.create_SubCategory('ArrayOfAction')

def duck_sub_ArrayOfHash(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='OrderedList')),\
	"[duck_sub_ArrayOfHash] parent_object must be of type OrderedList."




	return case_doc.create_SubCategory('ArrayOfHash')

def duck_sub_ArrayOfObject(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='OrderedList')),\
	"[duck_sub_ArrayOfObject] parent_object must be of type OrderedList."




	return case_doc.create_SubCategory('ArrayOfObject')

def duck_sub_ArrayOfString(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='OrderedList')),\
	"[duck_sub_ArrayOfString] parent_object must be of type OrderedList."




	return case_doc.create_SubCategory('ArrayOfString')

def duck_sub_AuthorizationType(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_AuthorizationType] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('AuthorizationType')

def duck_sub_ByteOrder(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_ByteOrder] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('ByteOrder')

def duck_sub_CompressionMethod(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_CompressionMethod] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('CompressionMethod')

def duck_sub_ConfigurationSetting(case_doc, parent_object, itemDescription=Missing(), itemName=Missing(), itemType=Missing(), itemValue=Missing()):
	'''
	:param itemName: Exactly 1 of type string.
	:param itemValue: Exactly 1 of type string.
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='SupportingClasses')),\
	"[duck_sub_ConfigurationSetting] parent_object must be of type SupportingClasses."

	assert not isinstance(itemName, Missing),\
	"[duck_sub_ConfigurationSetting] itemName is required."
	if not isinstance(itemName, Missing):
		assert isinstance(itemName, string),\
		"[duck_sub_ConfigurationSetting] itemName must be of type string."
	assert not isinstance(itemValue, Missing),\
	"[duck_sub_ConfigurationSetting] itemValue is required."
	if not isinstance(itemValue, Missing):
		assert isinstance(itemValue, string),\
		"[duck_sub_ConfigurationSetting] itemValue must be of type string."



	return case_doc.create_SubCategory('ConfigurationSetting', itemDescription=itemDescription, itemName=itemName, itemType=itemType, itemValue=itemValue)

def duck_sub_DataType(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_DataType] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('DataType')

def duck_sub_DeviceType(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_DeviceType] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('DeviceType')

def duck_sub_DictionaryItem(case_doc, parent_object, key=Missing()):
	'''
	:param key: Exactly 1 of type string.
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='SupportingClasses')),\
	"[duck_sub_DictionaryItem] parent_object must be of type SupportingClasses."

	assert not isinstance(key, Missing),\
	"[duck_sub_DictionaryItem] key is required."
	if not isinstance(key, Missing):
		assert isinstance(key, string),\
		"[duck_sub_DictionaryItem] key must be of type string."



	return case_doc.create_SubCategory('DictionaryItem', key=key)

def duck_sub_DiskPartitionType(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_DiskPartitionType] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('DiskPartitionType')

def duck_sub_DiskType(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_DiskType] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('DiskType')

def duck_sub_DomainName(case_doc, parent_object, isTLD=Missing()):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='SupportingClasses')),\
	"[duck_sub_DomainName] parent_object must be of type SupportingClasses."




	return case_doc.create_SubCategory('DomainName', isTLD=isTLD)

def duck_sub_EmailAddress(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='SupportingClasses')),\
	"[duck_sub_EmailAddress] parent_object must be of type SupportingClasses."




	return case_doc.create_SubCategory('EmailAddress')

def duck_sub_EncodingMethod(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_EncodingMethod] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('EncodingMethod')

def duck_sub_EncryptionMethod(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_EncryptionMethod] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('EncryptionMethod')

def duck_sub_EncryptionMode(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_EncryptionMode] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('EncryptionMode')

def duck_sub_ErrorType(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_ErrorType] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('ErrorType')

def duck_sub_FileMismatchType(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_FileMismatchType] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('FileMismatchType')

def duck_sub_FilePath(case_doc, parent_object, delimiter=Missing(), filePathSegments=Missing()):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='SupportingClasses')),\
	"[duck_sub_FilePath] parent_object must be of type SupportingClasses."




	return case_doc.create_SubCategory('FilePath', delimiter=delimiter, filePathSegments=filePathSegments)

def duck_sub_FileSystemType(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_FileSystemType] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('FileSystemType')

def duck_sub_GlobalFlagType(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_GlobalFlagType] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('GlobalFlagType')

def duck_sub_HashMethod(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_HashMethod] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('HashMethod')

def duck_sub_IPv4Address(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='SupportingClasses')),\
	"[duck_sub_IPv4Address] parent_object must be of type SupportingClasses."




	return case_doc.create_SubCategory('IPv4Address')

def duck_sub_IPv6Address(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='SupportingClasses')),\
	"[duck_sub_IPv6Address] parent_object must be of type SupportingClasses."




	return case_doc.create_SubCategory('IPv6Address')

def duck_sub_ImageCompressionMethod(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_ImageCompressionMethod] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('ImageCompressionMethod')

def duck_sub_ImageType(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_ImageType] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('ImageType')

def duck_sub_Language(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_Language] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('Language')

def duck_sub_MACAddress(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='SupportingClasses')),\
	"[duck_sub_MACAddress] parent_object must be of type SupportingClasses."




	return case_doc.create_SubCategory('MACAddress')

def duck_sub_MimePartType(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_MimePartType] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('MimePartType')

def duck_sub_MimeType(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_MimeType] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('MimeType')

def duck_sub_PEType(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_PEType] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('PEType')

def duck_sub_PasswordType(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_PasswordType] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('PasswordType')

def duck_sub_ReceivedEvent(case_doc, parent_object, receivedTime=Missing(), receiver=Missing()):
	'''
	:param receivedTime: Exactly 1 of type dateTimeStamp.
	:param receiver: Exactly 1 of type Trace.
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='SupportingClasses')),\
	"[duck_sub_ReceivedEvent] parent_object must be of type SupportingClasses."

	assert not isinstance(receivedTime, Missing),\
	"[duck_sub_ReceivedEvent] receivedTime is required."
	if not isinstance(receivedTime, Missing):
		assert isinstance(receivedTime, dateTimeStamp),\
		"[duck_sub_ReceivedEvent] receivedTime must be of type dateTimeStamp."
	assert not isinstance(receiver, Missing),\
	"[duck_sub_ReceivedEvent] receiver is required."
	if not isinstance(receiver, Missing):
		assert (isinstance(receiver, case.CoreCategory) and (receiver.type=="Trace")),\
		"[duck_sub_ReceivedEvent] receiver must be of type Trace."



	return case_doc.create_SubCategory('ReceivedEvent', receivedTime=receivedTime, receiver=receiver)

def duck_sub_ServiceStatus(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_ServiceStatus] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('ServiceStatus')

def duck_sub_Servicetype(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_Servicetype] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('Servicetype')

def duck_sub_StartType(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_StartType] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('StartType')

def duck_sub_URI(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='SupportingClasses')),\
	"[duck_sub_URI] parent_object must be of type SupportingClasses."




	return case_doc.create_SubCategory('URI')

def duck_sub_VisibilityType(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='Enumeration')),\
	"[duck_sub_VisibilityType] parent_object must be of type Enumeration."




	return case_doc.create_SubCategory('VisibilityType')

def duck_sub_WindowsPEFileHeader(case_doc, parent_object, characteristics=Missing(), machine=Missing(), numberOfSections=Missing(), numberOfSymbols=Missing(), optionalHeader=Missing(), pointerToSymbolTable=Missing(), sizeOfOptionalHeader=Missing(), timeDateStamp=Missing()):
	'''
	:param machine: Exactly 1 of type hexBinary.
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='SupportingClasses')),\
	"[duck_sub_WindowsPEFileHeader] parent_object must be of type SupportingClasses."

	assert not isinstance(machine, Missing),\
	"[duck_sub_WindowsPEFileHeader] machine is required."
	if not isinstance(machine, Missing):
		assert isinstance(machine, hexBinary),\
		"[duck_sub_WindowsPEFileHeader] machine must be of type hexBinary."



	return case_doc.create_SubCategory('WindowsPEFileHeader', characteristics=characteristics, machine=machine, numberOfSections=numberOfSections, numberOfSymbols=numberOfSymbols, optionalHeader=optionalHeader, pointerToSymbolTable=pointerToSymbolTable, sizeOfOptionalHeader=sizeOfOptionalHeader, timeDateStamp=timeDateStamp)

def duck_sub_WindowsPEOptionalHeader(case_doc, parent_object, addressOfEntryPoint=Missing(), baseOfCode=Missing(), checksum=Missing(), dllCharacteristics=Missing(), fileAlignment=Missing(), imageBase=Missing(), loaderFlags=Missing(), magic=Missing(), majorImageVersion=Missing(), majorOSVersion=Missing(), majorSubsystemVersion=Missing(), majorlinkerVersion=Missing(), minorImageVersion=Missing(), minorLinkerVersion=Missing(), minorOSVersion=Missing(), minorSubsystemVersion=Missing(), numberOfRVAAndSizes=Missing(), sectionAlignment=Missing(), sizeOfCode=Missing(), sizeOfHeaders=Missing(), sizeOfHeapCommit=Missing(), sizeOfHeapReserve=Missing(), sizeOfImage=Missing(), sizeOfInitializedData=Missing(), sizeOfStackCommit=Missing(), sizeOfStackReserve=Missing(), sizeOfUnintialializedData=Missing(), subsystem=Missing(), win32VersionValue=Missing()):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='SupportingClasses')),\
	"[duck_sub_WindowsPEOptionalHeader] parent_object must be of type SupportingClasses."




	return case_doc.create_SubCategory('WindowsPEOptionalHeader', addressOfEntryPoint=addressOfEntryPoint, baseOfCode=baseOfCode, checksum=checksum, dllCharacteristics=dllCharacteristics, fileAlignment=fileAlignment, imageBase=imageBase, loaderFlags=loaderFlags, magic=magic, majorImageVersion=majorImageVersion, majorOSVersion=majorOSVersion, majorSubsystemVersion=majorSubsystemVersion, majorlinkerVersion=majorlinkerVersion, minorImageVersion=minorImageVersion, minorLinkerVersion=minorLinkerVersion, minorOSVersion=minorOSVersion, minorSubsystemVersion=minorSubsystemVersion, numberOfRVAAndSizes=numberOfRVAAndSizes, sectionAlignment=sectionAlignment, sizeOfCode=sizeOfCode, sizeOfHeaders=sizeOfHeaders, sizeOfHeapCommit=sizeOfHeapCommit, sizeOfHeapReserve=sizeOfHeapReserve, sizeOfImage=sizeOfImage, sizeOfInitializedData=sizeOfInitializedData, sizeOfStackCommit=sizeOfStackCommit, sizeOfStackReserve=sizeOfStackReserve, sizeOfUnintialializedData=sizeOfUnintialializedData, subsystem=subsystem, win32VersionValue=win32VersionValue)

def duck_sub_WindowsPESection(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='SupportingClasses')),\
	"[duck_sub_WindowsPESection] parent_object must be of type SupportingClasses."




	return case_doc.create_SubCategory('WindowsPESection')

def duck_sub_WindowsRegistryValue(case_doc, parent_object, dataType=Missing()):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='SupportingClasses')),\
	"[duck_sub_WindowsRegistryValue] parent_object must be of type SupportingClasses."




	return case_doc.create_SubCategory('WindowsRegistryValue', dataType=dataType)

def duck_sub_X509V3Extensions(case_doc, parent_object, authorityKeyIdentifier=Missing(), basicContraints=Missing(), certificatePolicies=Missing(), crlDistributionPoints=Missing(), extendedKeyUsage=Missing(), inhibitAnyPolicy=Missing(), issuerAlternativeName=Missing(), keyUsage=Missing(), nameContraints=Missing(), policyConstraints=Missing(), policyMappings=Missing(), privateKeyUsagePeriodNotAfter=Missing(), privateKeyUsagePeriodNotBefore=Missing(), subjectAlternativeName=Missing(), subjectDirectoryAttribute=Missing(), subjectKeyIdentifier=Missing()):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='SupportingClasses')),\
	"[duck_sub_X509V3Extensions] parent_object must be of type SupportingClasses."




	return case_doc.create_SubCategory('X509V3Extensions', authorityKeyIdentifier=authorityKeyIdentifier, basicContraints=basicContraints, certificatePolicies=certificatePolicies, crlDistributionPoints=crlDistributionPoints, extendedKeyUsage=extendedKeyUsage, inhibitAnyPolicy=inhibitAnyPolicy, issuerAlternativeName=issuerAlternativeName, keyUsage=keyUsage, nameContraints=nameContraints, policyConstraints=policyConstraints, policyMappings=policyMappings, privateKeyUsagePeriodNotAfter=privateKeyUsagePeriodNotAfter, privateKeyUsagePeriodNotBefore=privateKeyUsagePeriodNotBefore, subjectAlternativeName=subjectAlternativeName, subjectDirectoryAttribute=subjectDirectoryAttribute, subjectKeyIdentifier=subjectKeyIdentifier)



#=====================================================
#-- DUCK SUB SUB

def duck_sub_sub_ActionLifecycle(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='ArrayOfAction')),\
	"[duck_sub_sub_ActionLifecycle] parent_object must be of type ArrayOfAction."




	return case_doc.create_SubCategory('ActionLifecycle')



#=====================================================
#-- PROP

def prop_AFFImage(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('AFFImage')

def prop_Account(core_object, accountIdentifier=Missing(), accountIssuer=Missing(), accountType=Missing(), isActive=Missing()):
	'''
	:param accountIdentifier: Exactly 1 of type string.
	:return: A PropertyBundle object.
	'''

	assert not isinstance(accountIdentifier, Missing),\
	"[prop_Account] accountIdentifier is required."
	if not isinstance(accountIdentifier, Missing):
		assert isinstance(accountIdentifier, string),\
		"[prop_Account] accountIdentifier must be of type string."



	return case_doc.create_PropertyBundle('Account', accountIdentifier=accountIdentifier, accountIssuer=accountIssuer, accountType=accountType, isActive=isActive)

def prop_AccountAuthentication(core_object, passwordLastChanged=Missing(), passwordType=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('AccountAuthentication', passwordLastChanged=passwordLastChanged, passwordType=passwordType)

def prop_ActionReferences(core_object, instrument=Missing(), performer=Missing(), result=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('ActionReferences', instrument=instrument, performer=performer, result=result)

def prop_AndroidPackage(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('AndroidPackage')

def prop_Application(core_object, applicationIdentifier=Missing(), numberOfLaunches=Missing(), operatingSystem=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('Application', applicationIdentifier=applicationIdentifier, numberOfLaunches=numberOfLaunches, operatingSystem=operatingSystem)

def prop_ApplicationAccount(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('ApplicationAccount')

def prop_ArchiveFile(core_object, comment=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('ArchiveFile', comment=comment)

def prop_Attachment(core_object, uri=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('Attachment', uri=uri)

def prop_Audio(core_object, audioType=Missing(), bitRate=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('Audio', audioType=audioType, bitRate=bitRate)

def prop_Authorization(core_object, authorizationIdentifier=Missing(), authorizationType=Missing()):
	'''
	:param authorizationIdentifier: At least 1 of type string.
	:param authorizationType: Exactly 1 of type AuthorizationType.
	:return: A PropertyBundle object.
	'''

	assert not isinstance(authorizationIdentifier, Missing),\
	"[prop_Authorization] authorizationIdentifier is required."
	if not isinstance(authorizationIdentifier, Missing):
		assert isinstance(authorizationIdentifier, list),\
		"[prop_Authorization] authorizationIdentifier must be of type List of string."
		assert all(isinstance(i, string) for i in authorizationIdentifier),\
		"[prop_Authorization] authorizationIdentifier must be of type List of string."
	assert not isinstance(authorizationType, Missing),\
	"[prop_Authorization] authorizationType is required."
	if not isinstance(authorizationType, Missing):
		assert (isinstance(authorizationType, case.DuckCategory) and (authorizationType.type=="AuthorizationType")),\
		"[prop_Authorization] authorizationType must be of type AuthorizationType."



	return case_doc.create_PropertyBundle('Authorization', authorizationIdentifier=authorizationIdentifier, authorizationType=authorizationType)

def prop_AutonomousSystem(core_object, asHandle=Missing(), number=Missing(), regionalInternetRegistry=Missing()):
	'''
	:param number: Exactly 1 of type int.
	:return: A PropertyBundle object.
	'''

	assert not isinstance(number, Missing),\
	"[prop_AutonomousSystem] number is required."
	if not isinstance(number, Missing):
		assert isinstance(number, int),\
		"[prop_AutonomousSystem] number must be of type int."



	return case_doc.create_PropertyBundle('AutonomousSystem', asHandle=asHandle, number=number, regionalInternetRegistry=regionalInternetRegistry)

def prop_BDEVolume(core_object, startupKey=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('BDEVolume', startupKey=startupKey)

def prop_BirthInformation(core_object, birthDate=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('BirthInformation', birthDate=birthDate)

def prop_BrowserBookmark(core_object, bookmarkPath=Missing(), urlTargeted=Missing(), visitCount=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('BrowserBookmark', bookmarkPath=bookmarkPath, urlTargeted=urlTargeted, visitCount=visitCount)

def prop_BrowserCookie(core_object, cookieName=Missing(), cookiePath=Missing(), isSecure=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('BrowserCookie', cookieName=cookieName, cookiePath=cookiePath, isSecure=isSecure)

def prop_BrowserHistory(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('BrowserHistory')

def prop_Calendar(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('Calendar')

def prop_CalendarEntry(core_object, attendant=Missing(), eventStatus=Missing(), eventType=Missing(), isPrivate=Missing(), recurrence=Missing(), remindTime=Missing(), subject=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('CalendarEntry', attendant=attendant, eventStatus=eventStatus, eventType=eventType, isPrivate=isPrivate, recurrence=recurrence, remindTime=remindTime, subject=subject)

def prop_Compression(core_object, compressionRatio=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('Compression', compressionRatio=compressionRatio)

def prop_ComputerSpecification(core_object, biosVersion=Missing(), cpuFamily=Missing(), totalRam=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('ComputerSpecification', biosVersion=biosVersion, cpuFamily=cpuFamily, totalRam=totalRam)

def prop_Contact(core_object, contactIdentifier=Missing(), contactName=Missing(), contactType=Missing(), firstName=Missing(), lastName=Missing(), middleName=Missing(), screenName=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('Contact', contactIdentifier=contactIdentifier, contactName=contactName, contactType=contactType, firstName=firstName, lastName=lastName, middleName=middleName, screenName=screenName)

def prop_ContentData(core_object, byteOrder=Missing(), dataPayload=Missing(), dataPayloadReferenceURL=Missing(), isEncrypted=Missing(), magicNumber=Missing(), mimeClass=Missing(), mimeType=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('ContentData', byteOrder=byteOrder, dataPayload=dataPayload, dataPayloadReferenceURL=dataPayloadReferenceURL, isEncrypted=isEncrypted, magicNumber=magicNumber, mimeClass=mimeClass, mimeType=mimeType)

def prop_DataRange(core_object, rangeOffset=Missing(), rangeOffsetType=Missing(), rangeSize=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('DataRange', rangeOffset=rangeOffset, rangeOffsetType=rangeOffsetType, rangeSize=rangeSize)

def prop_Device(core_object, deviceType=Missing(), model=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('Device', deviceType=deviceType, model=model)

def prop_DigitalAccount(core_object, accountLogin=Missing(), firstLoginTime=Missing(), isDisabled=Missing(), lastLoginTime=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('DigitalAccount', accountLogin=accountLogin, firstLoginTime=firstLoginTime, isDisabled=isDisabled, lastLoginTime=lastLoginTime)

def prop_Disk(core_object, diskSize=Missing(), diskType=Missing(), freeSpace=Missing(), hasPartition=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('Disk', diskSize=diskSize, diskType=diskType, freeSpace=freeSpace, hasPartition=hasPartition)

def prop_DiskPartition(core_object, diskPartitionType=Missing(), mountPoint=Missing(), partitionIdentifier=Missing(), partitionLength=Missing(), partitionOffset=Missing(), spaceLeft=Missing(), spaceUsed=Missing(), totalSpace=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('DiskPartition', diskPartitionType=diskPartitionType, mountPoint=mountPoint, partitionIdentifier=partitionIdentifier, partitionLength=partitionLength, partitionOffset=partitionOffset, spaceLeft=spaceLeft, spaceUsed=spaceUsed, totalSpace=totalSpace)

def prop_EWFImage(core_object, acquiryDate=Missing(), caseNumber=Missing(), description=Missing(), errorGranularity=Missing(), evidenceNumber=Missing(), examinerName=Missing(), guid=Missing(), notes=Missing(), operatingSystemUsed=Missing(), sectorsPerChunk=Missing(), softwareVersionUsed=Missing(), systemDate=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('EWFImage', acquiryDate=acquiryDate, caseNumber=caseNumber, description=description, errorGranularity=errorGranularity, evidenceNumber=evidenceNumber, examinerName=examinerName, guid=guid, notes=notes, operatingSystemUsed=operatingSystemUsed, sectorsPerChunk=sectorsPerChunk, softwareVersionUsed=softwareVersionUsed, systemDate=systemDate)

def prop_EXIF(core_object, exifData=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('EXIF', exifData=exifData)

def prop_EmailAccount(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('EmailAccount')

def prop_EmailMessage(core_object, bcc=Missing(), bodyMultipart=Missing(), bodyRaw=Missing(), cc=Missing(), contentDisposition=Missing(), contentType=Missing(), headerRaw=Missing(), inReplyTo=Missing(), isMimeEncoded=Missing(), isMultipart=Missing(), otherHeader=Missing(), receivedLine=Missing(), reference=Missing(), xMailer=Missing(), xOriginatingIP=Missing()):
	'''
	:param isMimeEncoded: Exactly 1 of type boolean.
	:param isMultipart: Exactly 1 of type boolean.
	:return: A PropertyBundle object.
	'''

	assert not isinstance(isMimeEncoded, Missing),\
	"[prop_EmailMessage] isMimeEncoded is required."
	if not isinstance(isMimeEncoded, Missing):
		assert isinstance(isMimeEncoded, boolean),\
		"[prop_EmailMessage] isMimeEncoded must be of type boolean."
	assert not isinstance(isMultipart, Missing),\
	"[prop_EmailMessage] isMultipart is required."
	if not isinstance(isMultipart, Missing):
		assert isinstance(isMultipart, boolean),\
		"[prop_EmailMessage] isMultipart must be of type boolean."



	return case_doc.create_PropertyBundle('EmailMessage', bcc=bcc, bodyMultipart=bodyMultipart, bodyRaw=bodyRaw, cc=cc, contentDisposition=contentDisposition, contentType=contentType, headerRaw=headerRaw, inReplyTo=inReplyTo, isMimeEncoded=isMimeEncoded, isMultipart=isMultipart, otherHeader=otherHeader, receivedLine=receivedLine, reference=reference, xMailer=xMailer, xOriginatingIP=xOriginatingIP)

def prop_Encoding(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('Encoding')

def prop_Encryption(core_object, encryptionIV=Missing(), encryptionKey=Missing(), encryptionMethod=Missing(), encryptionMode=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('Encryption', encryptionIV=encryptionIV, encryptionKey=encryptionKey, encryptionMethod=encryptionMethod, encryptionMode=encryptionMode)

def prop_Error(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('Error')

def prop_Event(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('Event')

def prop_ExtInode(core_object, extDeletionTime=Missing(), extFileType=Missing(), extFlags=Missing(), extHardLinkCount=Missing(), extInodeChangeTime=Missing(), extInodeID=Missing(), extPermissions=Missing(), extSGID=Missing(), extSUID=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('ExtInode', extDeletionTime=extDeletionTime, extFileType=extFileType, extFlags=extFlags, extHardLinkCount=extHardLinkCount, extInodeChangeTime=extInodeChangeTime, extInodeID=extInodeID, extPermissions=extPermissions, extSGID=extSGID, extSUID=extSUID)

def prop_ExtractedFeatures(core_object, extractedCodeSnippet=Missing(), extractedImport=Missing(), extractedString=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('ExtractedFeatures', extractedCodeSnippet=extractedCodeSnippet, extractedImport=extractedImport, extractedString=extractedString)

def prop_ExtractedString(core_object, byteStringValue=Missing(), englishTranslation=Missing(), language=Missing(), length=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('ExtractedString', byteStringValue=byteStringValue, englishTranslation=englishTranslation, language=language, length=length)

def prop_FVDEEncryption(core_object, encryptedRootPlist=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('FVDEEncryption', encryptedRootPlist=encryptedRootPlist)

def prop_File(core_object, extension=Missing(), fileName=Missing(), filePath=Missing(), isAllocated=Missing(), isDirectory=Missing(), metadataChangedTime=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('File', extension=extension, fileName=fileName, filePath=filePath, isAllocated=isAllocated, isDirectory=isDirectory, metadataChangedTime=metadataChangedTime)

def prop_FileMetadataMismatch(core_object, mismatchType=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('FileMetadataMismatch', mismatchType=mismatchType)

def prop_FilePermissions(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('FilePermissions')

def prop_FileSystem(core_object, clusterSize=Missing(), fileSystemType=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('FileSystem', clusterSize=clusterSize, fileSystemType=fileSystemType)

def prop_Fragment(core_object, fragmentIndex=Missing(), totalFragments=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('Fragment', fragmentIndex=fragmentIndex, totalFragments=totalFragments)

def prop_GeoLocationEntry(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('GeoLocationEntry')

def prop_GeoLocationLog(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('GeoLocationLog')

def prop_GeoLocationTrack(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('GeoLocationTrack')

def prop_HFSFileSystem(core_object, hfsBackupTime=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('HFSFileSystem', hfsBackupTime=hfsBackupTime)

def prop_HTTPConnection(core_object, httpMessageBodyData=Missing(), httpMessageBodyLength=Missing(), httpRequestHeader=Missing(), httpRequestLine=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('HTTPConnection', httpMessageBodyData=httpMessageBodyData, httpMessageBodyLength=httpMessageBodyLength, httpRequestHeader=httpRequestHeader, httpRequestLine=httpRequestLine)

def prop_Hash(core_object, hashMethod=Missing(), hashValue=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('Hash', hashMethod=hashMethod, hashValue=hashValue)

def prop_ICMPConnection(core_object, code=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('ICMPConnection', code=code)

def prop_IOSPackage(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('IOSPackage')

def prop_IdentityPropertyBundle(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('IdentityPropertyBundle')

def prop_Image(core_object, imageType=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('Image', imageType=imageType)

def prop_LVMVolume(core_object, volumeIndex=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('LVMVolume', volumeIndex=volumeIndex)

def prop_LatLongCoordinates(core_object, latitude=Missing(), longitude=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('LatLongCoordinates', latitude=latitude, longitude=longitude)

def prop_LinuxPackage(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('LinuxPackage')

def prop_Memory(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('Memory')

def prop_Message(core_object, isRead=Missing(), messageText=Missing(), messageType=Missing(), received=Missing(), sentTime=Missing(), sessionID=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('Message', isRead=isRead, messageText=messageText, messageType=messageType, received=received, sentTime=sentTime, sessionID=sessionID)

def prop_MessageThread(core_object, messages=Missing(), visibility=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('MessageThread', messages=messages, visibility=visibility)

def prop_MftRecord(core_object, mftFileID=Missing(), mftFileNameAccessedTime=Missing(), mftFileNameCreatedTime=Missing(), mftFileNameLength=Missing(), mftFileNameModifiedTime=Missing(), mftFileNameRecordChangeTime=Missing(), mftFlags=Missing(), mftParentID=Missing(), mftRecordChangeTime=Missing(), ntfsHardLinkCount=Missing(), ntfsOwnerID=Missing(), ntfsOwnerSID=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('MftRecord', mftFileID=mftFileID, mftFileNameAccessedTime=mftFileNameAccessedTime, mftFileNameCreatedTime=mftFileNameCreatedTime, mftFileNameLength=mftFileNameLength, mftFileNameModifiedTime=mftFileNameModifiedTime, mftFileNameRecordChangeTime=mftFileNameRecordChangeTime, mftFlags=mftFlags, mftParentID=mftParentID, mftRecordChangeTime=mftRecordChangeTime, ntfsHardLinkCount=ntfsHardLinkCount, ntfsOwnerID=ntfsOwnerID, ntfsOwnerSID=ntfsOwnerSID)

def prop_Mutex(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('Mutex')

def prop_NTFSFileSystem(core_object, alternateDataStream=Missing(), sid=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('NTFSFileSystem', alternateDataStream=alternateDataStream, sid=sid)

def prop_NetworkConnection(core_object, destination=Missing(), protocols=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('NetworkConnection', destination=destination, protocols=protocols)

def prop_NetworkLocation(core_object, ipAddress=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('NetworkLocation', ipAddress=ipAddress)

def prop_NetworkPacket(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('NetworkPacket')

def prop_NetworkRoute(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('NetworkRoute')

def prop_NetworkSocket(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('NetworkSocket')

def prop_NetworkSubnet(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('NetworkSubnet')

def prop_OperatingSystem(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('OperatingSystem')

def prop_PDFFile(core_object, documentInformation=Missing(), isOptimized=Missing(), pdfId0=Missing(), pdfId1=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('PDFFile', documentInformation=documentInformation, isOptimized=isOptimized, pdfId0=pdfId0, pdfId1=pdfId1)

def prop_Package(core_object, applicationName=Missing(), dataPath=Missing(), packageName=Missing(), packagePermission=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('Package', applicationName=applicationName, dataPath=dataPath, packageName=packageName, packagePermission=packagePermission)

def prop_PathRelation(core_object, path=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('PathRelation', path=path)

def prop_PhoneAccount(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('PhoneAccount')

def prop_PhoneCall(core_object, callType=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('PhoneCall', callType=callType)

def prop_Process(core_object, arguments=Missing(), binary=Missing(), creatorUser=Missing(), currentWorkingDirectory=Missing(), environmentVariable=Missing(), isHidden=Missing(), parentProcess=Missing(), pid=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('Process', arguments=arguments, binary=binary, creatorUser=creatorUser, currentWorkingDirectory=currentWorkingDirectory, environmentVariable=environmentVariable, isHidden=isHidden, parentProcess=parentProcess, pid=pid)

def prop_QCOWImage(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('QCOWImage')

def prop_RasterPicture(core_object, bitsPerPixel=Missing(), imageCompressionMethod=Missing(), imageHeight=Missing(), imageWidth=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('RasterPicture', bitsPerPixel=bitsPerPixel, imageCompressionMethod=imageCompressionMethod, imageHeight=imageHeight, imageWidth=imageWidth)

def prop_SMSMessage(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('SMSMessage')

def prop_SQLiteBlob(core_object, columnName=Missing(), rowCondition=Missing(), rowIndex=Missing(), tableName=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('SQLiteBlob', columnName=columnName, rowCondition=rowCondition, rowIndex=rowIndex, tableName=tableName)

def prop_SimpleAddress(core_object, country=Missing(), locality=Missing(), postalCode=Missing(), region=Missing(), street=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('SimpleAddress', country=country, locality=locality, postalCode=postalCode, region=region, street=street)

def prop_SimpleName(core_object, familyName=Missing(), givenName=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('SimpleName', familyName=familyName, givenName=givenName)

def prop_SymbolicLink(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('SymbolicLink')

def prop_System(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('System')

def prop_TCPConnection(core_object, destinationFlags=Missing(), sourceFlags=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('TCPConnection', destinationFlags=destinationFlags, sourceFlags=sourceFlags)

def prop_ToolArguments(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('ToolArguments')

def prop_ToolConfiguration(core_object, configurationSetting=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('ToolConfiguration', configurationSetting=configurationSetting)

def prop_UDPConnection(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('UDPConnection')

def prop_UNIXAccount(core_object, gid=Missing(), shell=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('UNIXAccount', gid=gid, shell=shell)

def prop_UNIXNetworkRoute(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('UNIXNetworkRoute')

def prop_UNIXProcess(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('UNIXProcess')

def prop_UNIXVolume(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('UNIXVolume')

def prop_UserAccount(core_object, canEscalatePrivs=Missing(), homeDirectory=Missing(), isPrivileged=Missing(), isServiceAccount=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('UserAccount', canEscalatePrivs=canEscalatePrivs, homeDirectory=homeDirectory, isPrivileged=isPrivileged, isServiceAccount=isServiceAccount)

def prop_VShadow(core_object, snapshotID=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('VShadow', snapshotID=snapshotID)

def prop_Volume(core_object, sectorSize=Missing(), volumeID=Missing(), volumeType=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('Volume', sectorSize=sectorSize, volumeID=volumeID, volumeType=volumeType)

def prop_WHOIS(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('WHOIS')

def prop_WindowsAccount(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('WindowsAccount')

def prop_WindowsActiveDirectoryAccount(core_object, objectGUID=Missing()):
	'''
	:param objectGUID: Exactly 1 of type string.
	:return: A PropertyBundle object.
	'''

	assert not isinstance(objectGUID, Missing),\
	"[prop_WindowsActiveDirectoryAccount] objectGUID is required."
	if not isinstance(objectGUID, Missing):
		assert isinstance(objectGUID, string),\
		"[prop_WindowsActiveDirectoryAccount] objectGUID must be of type string."



	return case_doc.create_PropertyBundle('WindowsActiveDirectoryAccount', objectGUID=objectGUID)

def prop_WindowsComputerSpecification(core_object, globalFlagList=Missing(), msProductID=Missing(), msProductName=Missing(), netBiosName=Missing(), registeredOrganization=Missing(), registeredOwner=Missing(), windowsDirectory=Missing(), windowsDomain=Missing(), windowsSystemDirectory=Missing(), windowsTempDirectory=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('WindowsComputerSpecification', globalFlagList=globalFlagList, msProductID=msProductID, msProductName=msProductName, netBiosName=netBiosName, registeredOrganization=registeredOrganization, registeredOwner=registeredOwner, windowsDirectory=windowsDirectory, windowsDomain=windowsDomain, windowsSystemDirectory=windowsSystemDirectory, windowsTempDirectory=windowsTempDirectory)

def prop_WindowsMutex(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('WindowsMutex')

def prop_WindowsNetworkRoute(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('WindowsNetworkRoute')

def prop_WindowsPEBinaryFile(core_object, fileHeader=Missing(), impHash=Missing(), peType=Missing(), sections=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('WindowsPEBinaryFile', fileHeader=fileHeader, impHash=impHash, peType=peType, sections=sections)

def prop_WindowsPackage(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('WindowsPackage')

def prop_WindowsPrefetch(core_object, accessedDirectory=Missing(), accessedFile=Missing(), applicationFileName=Missing(), firstRunTime=Missing(), lastRunTime=Missing(), prefetchHash=Missing(), timesExecuted=Missing(), volume=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('WindowsPrefetch', accessedDirectory=accessedDirectory, accessedFile=accessedFile, applicationFileName=applicationFileName, firstRunTime=firstRunTime, lastRunTime=lastRunTime, prefetchHash=prefetchHash, timesExecuted=timesExecuted, volume=volume)

def prop_WindowsProcess(core_object, aslrEnabled=Missing(), depEnabled=Missing(), ownerSID=Missing(), startupInfo=Missing(), windowsTitle=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('WindowsProcess', aslrEnabled=aslrEnabled, depEnabled=depEnabled, ownerSID=ownerSID, startupInfo=startupInfo, windowsTitle=windowsTitle)

def prop_WindowsRegistryHive(core_object, hiveType=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('WindowsRegistryHive', hiveType=hiveType)

def prop_WindowsRegistryKey(core_object, creator=Missing(), numberOfSubkeys=Missing(), registryKey=Missing(), registryValue=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('WindowsRegistryKey', creator=creator, numberOfSubkeys=numberOfSubkeys, registryKey=registryKey, registryValue=registryValue)

def prop_WindowsService(core_object, serviceDescription=Missing(), serviceStatus=Missing(), serviceType=Missing(), startCommandLine=Missing(), startType=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('WindowsService', serviceDescription=serviceDescription, serviceStatus=serviceStatus, serviceType=serviceType, startCommandLine=startCommandLine, startType=startType)

def prop_WindowsSystem(core_object):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('WindowsSystem')

def prop_WindowsVolume(core_object, driveLetter=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('WindowsVolume', driveLetter=driveLetter)

def prop_X509Certificate(core_object, isSelfSigned=Missing(), issuer=Missing(), signatureAlgorithm=Missing(), subjectPublicKeyAlgorithm=Missing(), subjectPublicKeyExponent=Missing(), subjectPublicKeyModulus=Missing(), validityNotAfter=Missing(), validityNotBefore=Missing(), x509V3Extensions=Missing()):
	'''
	:return: A PropertyBundle object.
	'''




	return case_doc.create_PropertyBundle('X509Certificate', isSelfSigned=isSelfSigned, issuer=issuer, signatureAlgorithm=signatureAlgorithm, subjectPublicKeyAlgorithm=subjectPublicKeyAlgorithm, subjectPublicKeyExponent=subjectPublicKeyExponent, subjectPublicKeyModulus=subjectPublicKeyModulus, validityNotAfter=validityNotAfter, validityNotBefore=validityNotBefore, x509V3Extensions=x509V3Extensions)



#=====================================================
#-- PROP SUB

def prop_sub_CountriesOfResidence(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.PropertyBundle) and parent_object.type=='IdentityPropertyBundle')),\
	"[prop_sub_CountriesOfResidence] parent_object must be of type IdentityPropertyBundle."




	return case_doc.create_SubCategory('CountriesOfResidence')

def prop_sub_Occupation(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.PropertyBundle) and parent_object.type=='IdentityPropertyBundle')),\
	"[prop_sub_Occupation] parent_object must be of type IdentityPropertyBundle."




	return case_doc.create_SubCategory('Occupation')

def prop_sub_OrganizationDetails(case_doc, parent_object):
	'''
	:return: A SubCategory object.
	'''

	assert (isinstance(parent_object, case.PropertyBundle) and parent_object.type=='IdentityPropertyBundle')),\
	"[prop_sub_OrganizationDetails] parent_object must be of type IdentityPropertyBundle."




	return case_doc.create_SubCategory('OrganizationDetails')

