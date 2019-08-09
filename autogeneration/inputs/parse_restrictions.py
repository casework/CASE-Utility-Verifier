# NOTICE
# 
# This software was produced for the U.S. Government under
# contract SB-1341-14-CQ-0010, and is subject to the Rights
# in Data-General Clause 52.227-14, Alt. IV (DEC 2007)
#
# (c) 2018 The MITRE Corporation. All Rights Reserved.


#====================================================
import sys
import pprint
input_file  = sys.argv[1]



class Restrictions(object):
    """
    This class is for obtaining all restrictive OWL fields that are not
    (and cannot because of triples only having 3 objects) parsed by Ontospy.
    Input files parsed by Ontospy must be parsed separately again for these attributes
    lest this alteration be done in rdflib.parse itself (harder to update and maintain).
    """

    def __init__(self, input_file, namespaces, onto_keys, prop_keys):
        self.onto_file = input_file
        self.onto_keys = onto_keys
        self.prop_keys = prop_keys
        self.namespaces= namespaces
        self.card_dict = {}
        # Add dictionaries for other restrictions if needed.

        self.pp = pprint.PrettyPrinter(indent=4)


    def parse(self, cardinality):
        "This function will parse the input ontology file to obtain cardinalities (not already parsed with Python's RDFlib)."

        nlg_type = None
        prop = None
        with open(self.onto_file, 'r') as source:
            for line in source:
#                print(line)
                begin_entry = 0

                # These lines detect the beginning of new entries and may need modification if the CASE Turtle syntax changes.
                # Currently it handles v0.1.0 and v0.2.0 .
                for ns in self.namespaces:
                    if (ns in line) and ('###' in line):     #v0.1.0
                        begin_entry = 1
                    elif (ns in line) and (' ' not in line): #v0.2.0
                        begin_entry = 1

                # Grab NLG type.
                if begin_entry == 1:
                    if '#' not in line:
                        continue
                    spltz = line.split('#')
                    nlg_type = spltz[-1].strip('>\n')
#                    print '\nLINE'
#                    print nlg_type

                elif ('@prefix' in line) or ('@base' in line):
                    continue

                # If property in line.
                elif 'owl:onProperty' in line:
                    spltz = line.strip().strip(';').strip().split(' ')
                    prop  = spltz[-1].strip(':')
                    if '#' in prop:
                        prop = prop.split('#')
                        prop = prop[-1].strip('>')
#                    print 'PROPERTY\t', prop

                # If cardinality in line.
                elif ('cardinality' in line.lower()) and (len(line) - len(line.lstrip()) != 0):
                    spltz = line.strip().strip(';').strip().split(' ')
                    for part in spltz:
                        if 'cardinality' in part.lower():
                            card_field = part.split('owl:')[-1]
#                            print 'CARD_FIELD\t', card_field
                        if '^^xsd:' in part:
                            card_value = part.split('^^xsd:')[0].strip('"')
                            card_type  = part.split('^^xsd:')[1]
#                            print 'CARD_VALUE\t', card_value
#                            print 'CARD_TYPE\t', card_type


                    if nlg_type not in self.card_dict.keys():
                        self.card_dict[nlg_type] = {}
                    self.card_dict[nlg_type][prop] = {}
                    self.card_dict[nlg_type][prop]['card-field'] = card_field
                    self.card_dict[nlg_type][prop]['card-value'] = card_value
                    self.card_dict[nlg_type][prop]['card-type']  = card_type


                # Assume cardinality of 0-N if cardinality not present in line.
                elif line.strip() and nlg_type != None:
                    card_field = 'noCardinality'
                    card_value = 'any'
                    card_type  = 'string' # IS THIS CORRECT? What if it is 0-N of an int?

                    if nlg_type not in self.card_dict.keys():
                        self.card_dict[nlg_type] = {}
                    self.card_dict[nlg_type][prop] = {}
                    self.card_dict[nlg_type][prop]['card-field'] = card_field
                    self.card_dict[nlg_type][prop]['card-value'] = card_value
                    self.card_dict[nlg_type][prop]['card-type']  = card_type


                else:
                    # Skip lines that do not have property, cardinality, or nlg_type (begin_entry==1).
                    continue

#            self.pp.pprint(self.card_dict)
        return self.card_dict
