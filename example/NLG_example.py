# NOTICE
# 
# This software was produced for the U.S. Government under
# contract SB-1341-14-CQ-0010, and is subject to the Rights
# in Data-General Clause 52.227-14, Alt. IV (DEC 2007)
#
# (c) 2018 The MITRE Corporation. All Rights Reserved.


#====================================================
# CASE NLG VERIFIER v0.1.0

"""
The Natural Language Glossary (NLG) is an alphabetical list of types of CASE classes (categories of CASE types).
The functions in this file create CASE objects (instances of such types) while automatically checking ontology and type.
The API (case_example.py) could be used directly to create non-typed objects if ontology and type checking are not requirements.
However, we advise against this to maintain consistency across community usage of the ontology.

Note that different versions of the NLG exist for different realizations of the Unified Cyber Ontology.
The human legible NLG corresponding to this version of CASE (one realization of UCO) can be found here:
https://casework.github.io/case/case-v0.1.0-natural-language-glossary.html

-----------------------------------------------------
NOTES ON FUNCTION STRUCTURE

    CASE objects:         Search "CREATE A CASE OBJECT" in the API (case_example.py) to understand the high-level CASE objects.
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


import case_example
import sys
import unittest
import datetime

class Missing(object):
    def __init__(self):
        self.is_missing = True


#====================================================
#-- CORE IN ALPHABETICAL ORDER

def core_Action(uco_document, action_status=Missing(), start_time=Missing(), end_time=Missing(), errors=Missing(),
                action_count=Missing(), subaction_refs=Missing(), **kwargs):
    '''
    :param ActionStatus: At most one occurrence of type ControlledVocabulary.
    :param StartTime: At most one value of type Timestamp.
    :param EndTime: At most one value of type Timestamp.
    :param Errors: Any number of values of any type.
    :param ActionCount: At most one value of PositiveInteger.
    :param SubactionRefs: Any number of occurrences of Action.
    :return: A CoreObject object.
    '''

    if not isinstance(action_status, Missing):
        assert (isinstance(action_status, case_example.CoreObject) and (action_status.type=='ControlledVocabulary')),\
        "[core_Action] action_status must be of type ControlledVocab."
    if not isinstance(start_time, Missing):
        assert isinstance(start_time, datetime.datetime),\
        "[core_Action] start_time must be of type Timestamp."
    if not isinstance(end_time, Missing):
        assert isinstance(end_time, datetime.datetime),\
        "[core_Action] end_time must be of type Timestamp."
    #NOCHECK:errors
    if not isinstance(action_count, Missing):
        assert (isinstance(action_count, int) and (action_count > 0)),\
        "[core_Action] action_count must be of type Int and positive."
    if not isinstance(subaction_refs, Missing):
        assert isinstance(subaction_refs, list),\
        "[core_Action] subaction_refs must be of type List of Action."
        assert all( (isinstance(i, case_example.CoreObject) and i.type=='Action') for i in subaction_refs),\
        "[core_Action] subaction_refs must be of type List of Action."

    return uco_document.create_CoreObject('Action', ActionStatus=action_status, StartTime=start_time, EndTime=end_time, Errors=errors, ActionCount=action_count, SubactionRefs=subaction_refs, **kwargs)


def core_ControlledVocabulary(uco_document, value=Missing(), constraining_vocabulary_name=Missing(), constraining_vocabulary_ref=Missing(), **kwargs):
    '''
    :param Value: Exactly one value of type String.
    :param ConstrainingVocabularyName: At most one value of type String.
    :param ConstrainingVocabularyReference: At most one value of type URI.
    :return: A CoreObject object.
    '''

    assert not isinstance(value, Missing),\
    "[core_ControlledVocabulary] value is required."
    if not isinstance(value, Missing):
        assert isinstance(value, str),\
        "[core_ControlledVocabulary] value must be of type String."

    if not isinstance(constraining_vocabulary_name, Missing):
        assert isinstance(constraining_vocabulary_name, str),\
        "[core_ControlledVocabulary] constraining_vocabulary_name must be of type URI."
    #TODO:URI

    return uco_document.create_CoreObject('ControlledVocabulary', Value=value, ConstrainingVocabularyName=constraining_vocabulary_name, ConstrainingVocabularyRef=constraining_vocabulary_ref, **kwargs)


def core_Identity(uco_document, **kwargs):
    '''
    :return: A CoreObject object.
    '''

    #TODO:NothingElseToCheck

    return uco_document.create_CoreObject('Identity', **kwargs)


def core_MarkingDefinition(uco_document, definition_type=Missing(), definition=Missing(), **kwargs):
    '''
    :param DefinitionType: Exactly one value of type String.
    :param Definition: Any number of occurrences of MarkingModel.
    :return: A CoreObject object.
    '''

    assert not isinstance(definition_type, Missing),\
    "[core_MarkingDefinition] defintion_type is required."
    if not isinstance(definition_type, Missing):
        assert isinstance(definition_type, str),\
        "[core_MarkingDefinition] definition_type must be of type String."

    if not isinstance(definition, Missing):
        assert isinstance(definition, list),\
        "[core_MarkingDefinition] definition must be of type List of MarkingModel."
        assert all( (isinstance(i, case_example.DuckObject) and i.type=='MarkingModel') for i in definition),\
        "[core_MarkingDefinition] definition must be of type List of MarkingModel."

    return uco_document.create_CoreObject('MarkingDefinition', DefinitionType=definition_type, Definition=definition, **kwargs)


def core_Tool(uco_document, name=Missing(), version=Missing(), tool_type=Missing(), service_pack=Missing(), creator=Missing(), references=Missing(), **kwargs):
    '''
    :param Name: At most one value of type String.
    :param Version: At most one value of type String.
    :param ToolType: At most one value of type String.
    :param ServicePack: At most one value of type String.
    :param Creator: At most one value of type String.
    :param References: Any number of values of URI.
    :return: A CoreObject object.
    '''

    if not isinstance(name, Missing):
        assert isinstance(name, str),\
        "[core_Tool] name must be of type String."
    if not isinstance(version, Missing):
        assert isinstance(version, str),\
        "[core_Tool] version must be of type String."
    if not isinstance(tool_type, Missing):
        assert isinstance(tool_type, str),\
        "[core_Tool] tool_type must be of type String."
    if not isinstance(service_pack, Missing):
        assert isinstance(service_pack, str),\
        "[core_Tool] service_pack must be of type String."
    if not isinstance(creator, Missing):
        assert isinstance(creator, str),\
        "[core_Tool] creator must be of type String."
    #TODO:URI
    #check for list and then URI type

    return uco_document.create_CoreObject('Tool', Name=name, Version=version, ToolType=tool_type, ServicePack=service_pack, Creator=creator, References=references, **kwargs)


#====================================================
#-- CORE CHILDREN IN ALPHABETICAL ORDER

def core_sub_ForensicAction(uco_document, uco_object, **kwargs):
    '''
    :return: A SubObject object.
    '''

    assert (isinstance(uco_object, case_example.CoreObject) and (uco_object.type=='Action')),\
    "[core_sub_ForensicAction] uco_object must be of type Action."

    #TODO:NothingElseToCheck

    return uco_document.create_SubObject('ForensicAction', **kwargs)


#====================================================
#-- CONTEXT IN ALPHABETICAL ORDER

def context_Grouping(uco_document, context_strings=Missing(), **kwargs):
    '''
    :param Context: Any number of values of type String.
    :return: A ContextObject object.
    '''

    if not isinstance(context_strings, Missing):
        assert isinstance(context_strings, list),\
        "[context_Grouping] context_strings must be of type List of String."
        assert all(isinstance(i, str) for i in context_strings),\
        "[context_Grouping] context_strings must be of type List of String."

    return uco_document.create_ContextObject('Grouping', ContextStrings=context_strings, **kwargs)


#====================================================
#-- CONTEXT CHILDREN IN ALPHABETICAL ORDER

    # NO CONTEXT CHILDREN USED IN EXAMPLE


#====================================================
#-- PROPERTYBUNDLES IN ALPHABETICAL ORDER

def propbundle_Account(uco_object, account_id=Missing(), expiration_time=Missing(), created_time=Missing(), account_type=Missing(),
                account_issuer_ref=Missing(), is_active=Missing(), modified_time=Missing(), owner_ref=Missing(), **kwargs):
    '''
    :param AccoundID: Exactly one value of type String.
    :param ExprationTime: At most one value of type Timestamp.
    :param CreatedTime: At most one value of type Timestamp.
    :param AccountType: At most one occurrence of type ControlledVocabulary.
    :param AccountIssuerRef: At most one occurrence of type CoreObject.
    :param IsActive: At most one value of type Bool.
    :param ModifiedTime: At most one value of type Timestamp.
    :param OwnerRef: At most one occurrence of type CoreObject.
    :return: A PropertyBundle object.
    '''
    
    assert not isinstance(account_id, Missing),\
    "[propbundle_Account] account_id is required."
    if not isinstance(account_id, Missing):
        assert isinstance(account_id, str),\
        "[propbundle_Account] account_id must be of type String."

    if not isinstance(expiration_time, Missing):
        assert isinstance(expiration_time, datetime.datetime),\
        "[propbundle_Account] expiration_time must be of type Timestamp."
    if not isinstance(created_time, Missing):
        assert isinstance(created_time, datetime.datetime),\
        "[propbundle_Account] created_time must be of type TimeStamp."
    if not isinstance(account_type, Missing):
        assert (isinstance(account_type, case_example.CoreObject) and (account_type.type=='ControlledVocabulary')),\
        "[propbundle_Account] account_type must be of type ControlledVocabulary."
    if not isinstance(account_issuer_ref, Missing):
        assert isinstance(account_issuer_ref, case_example.CoreObject),\
        "[propbundle_Account] account_issuer_ref must be of type CoreObject."
    if not isinstance(is_active, Missing):
        assert isinstance(is_active, bool),\
        "[propbundle_Account] is_active must be of type Bool."
    if not isinstance(modified_time, Missing):
        assert isinstance(modified_time, datetime.datetime),\
        "[propbundle_Account] modified_time must be of type Timestamp."
    if not isinstance(owner_ref, Missing):
        assert isinstance(owner_ref, case_example.CoreObject),\
        "[propbundle_Account] owner_ref must be of type CoreObject."

    return uco_object.create_PropertyBundle('Account', AccoundID=account_id, ExpirationTime=expiration_time, CreatedTime=created_time,  AccountType=account_type, AccountIssuerRef=account_issuer_ref, IsActive=is_active, ModifiedTime=modified_time, OwnerRef=owner_ref, **kwargs)


def propbundle_Identity(uco_object, **kwargs):
    '''
    :return: A PropertyBundle object.
    '''

    #TODO:NothingElseToCheck

    return uco_object.create_PropertyBundle('Identity', **kwargs)


#====================================================
#-- PROPERTYBUNDLE CHILDREN IN ALPHABETICAL ORDER

def propbundle_sub_SimpleName(uco_document, uco_object_propbundle, family_name=Missing(), given_name=Missing(), honorific_prefix=Missing(), honorific_suffix=Missing(), **kwargs):
    '''
    :param FamilyName: Any number of values of any type.
    :param GivenName: Any number of values of any type.
    :param HonorificPrefix: Any number of values of any type.
    :param HonorificSuffix: Any number of values of any type.
    :return: A SubObject object.
    '''

    assert (isinstance(uco_object_propbundle, case_example.PropertyBundle) and (uco_object_propbundle.type=='Identity')),\
    "[propbundle_sub_SimpleName] uco_object_propbundle must be of type Identity."

    #TODO:NothingElseToCheck

    return uco_document.create_SubObject('ForensicAction', FamilyName=family_name, GivenName=given_name, HonorificPrefix=honorific_prefix, HonorificSuffix=honorific_suffix, **kwargs)


#====================================================
#-- DUCK IN ALPHABETICAL ORDER

def duck_MarkingModel(uco_document, **kwargs):
    '''
    :return: A DuckObject object.
    '''

    #TODO:NothingElseToCheck

    return uco_document.create_DuckObject('MarkingModel', **kwargs)


#====================================================
#-- DUCK CHILDREN IN ALPHABETICAL ORDER

    # NO DUCK CHILDREN USED IN EXAMPLE


#====================================================
#-- SPECIAL TYPE-CHECKING FUNCTIONS

    # NO SPECIAL TYPE-CHECKING USED IN EXAMPLE

