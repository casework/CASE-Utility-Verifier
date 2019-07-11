# NOTICE
# 
# This software was produced for the U.S. Government under
# contract SB-1341-14-CQ-0010, and is subject to the Rights
# in Data-General Clause 52.227-14, Alt. IV (DEC 2007)
#
# (c) 2018 The MITRE Corporation. All Rights Reserved.


#====================================================
from NLG_example import *
import case_example
import datetime

doc = case_example.Document()

print '~~~~~~~~~~ START'

#====================================================

core_example_1          = core_Identity(doc)
print "Obj1: ", core_example_1

#====================================================

core_example_2          = core_Tool(doc,
    name                = 'Super Frag-ilistic',
    version             = '0.12.3',
    # Custom properties can be injected into CASE objects.
    # Misspelled property names skip validation so be careful!
    custm_prop          = 'everything in its right place',
    tool_type           = 'Fragmentation',
    # Parameters may be optional.
    #service_pack        = 'MysteryBox',
    creator             = 'Carl Poppa')
print "Obj2: ", core_example_2

propbundle_example_1    = propbundle_Account(core_example_2,
    account_id          = 'Accnt324',
    expiration_time     = datetime.datetime.utcnow(),
    created_time        = datetime.datetime.utcnow(),
    account_type        = core_ControlledVocabulary(doc,
                                                    value                        = 'temp',
                                                    constraining_vocabulary_name = 'temporary'),
    account_issuer_ref  = core_example_1,
    is_active           = False,
    modified_time       = datetime.datetime.utcnow(),
    owner_ref           = core_example_1)
print "Obj3: ", propbundle_example_1

#====================================================

context_example         = context_Grouping(doc,
    context_strings     = ['the','teh','hte','het','eth','eht'])
    # Properties listed as 'any number of' must be lists. List members are checked for type as well.
    #context_strings     = 'the')
    #context_strings     = ['the',34,'eht'])
print "Obj4: ", context_example

#====================================================

core_example_3          = core_Action(doc,
    start_time          = datetime.datetime.utcnow())
print "Obj5: ", core_example_3

sub_example_1           = core_sub_ForensicAction(doc, core_example_3)
print "Obj6: ", sub_example_1

#====================================================

propbundle_example_2    = propbundle_Identity(core_example_3)
print "Obj7: ", propbundle_example_2

sub_example_2           = propbundle_sub_SimpleName(doc, propbundle_example_2,
                                                    honorific_prefix = 'Mr.',
                                                    given_name       = 'Bond')
print "Obj8: ", sub_example_2

#====================================================

duck_example            = duck_MarkingModel(doc)
print "Obj9: ", duck_example

#====================================================

print '~~~~~~~~~~  END'

doc.serialize(format='json-ld', destination='output_example.json')
#doc.serialize_append(format='json-ld', destination='output_example.json')
