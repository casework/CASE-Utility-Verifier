# NOTICE
# 
# This software was produced for the U.S. Government under
# contract SB-1341-14-CQ-0010, and is subject to the Rights
# in Data-General Clause 52.227-14, Alt. IV (DEC 2007)
#
# (c) 2018 The MITRE Corporation. All Rights Reserved.


#=====================================================
# Autogeneration currently only supports v0.1.0 and v0.2.0 for CASE/UCO.

import sys
from cStringIO import StringIO
import pprint
import rdflib
from ontospy import *
from inputs import parse_restrictions

input_file = sys.argv[1]        #Convert this to ArgParse if we decide to have flags, etc.

#=====================================================
#TODO

#Cardinality constraints may cause checks to be altered. Checks should be moved to a separate function where the correct constraint is written based on the cardinality, even if the value is not 0 or 1. (e.g. maxQualifiedCarinality = 3).
#Rename CoreObject to CoreCategory, DuckCategory, etc.
#Require cardinality field in all properties where a check will be performed.
#Have debug statements / lists of errors / unknown objects printed to an output file/screen at end.
#Missing() class can be replaced as noted in Python-API Github issue.

#Implement known namespaces and known native-types lists for better error handling. (e.g. current case.ttl has 'boolean' instead of 'bool' and 'Timestamp' instead of 'datetime'
# Note that native types should be used in the CASE RDF specification as well.
    # (e.g. 'datetime' instead of 'Timestamp')
    # Ideally there should be a check here to see if the type is in a list of known supported types and throw error if not.


#=====================================================
# ADD DEBUG FUNCTION HERE TO CALL AND PASS PRINT STRINGS TO.
# IF DEBUG IS ON (PASSED IN FROM CMD) WILL PRINT, OTHERWISE NOT.
# ALTERNATIVELY PUT PRINT STATEMENTS IN FUNCTION AND HAVE FUNCTION CALL
# INDICATE WHICH STRING TO PRINT.

debugging   = False
debug_out   = False
debug_txt   = open('outputs/debug.txt','w')
debug_txt.truncate()

def debug_print(text):
    if debugging==True:
        print text
        print ""
    if debug_out==True:
        debug_txt.write(text)
        debug_txt.write("\n\n")
pp = pprint.PrettyPrinter(indent=4)


#=====================================================
# WRITE BODY ASSERTS (MINUS PARENT OBJECTS)

def write_body_assert(prop, p_required, prop_dict, dict_dict, card_field, card_type, card_value, is_list_type, tab, f_name,  body_assert_types):

    prop_types = prop_dict[prop]
    if len(prop_types) > 1:
        debug_print("Property ({}) has multiple types specified:\n{}\n".format(prop, prop_types))
        return ""
    else:
        p_type = prop_types[0]
        p_type_found = False
        fc_where_found = None
        fc_object = None
        check_type = None
        if p_type == 'UcoObject':
           check_type = 'CASE-Object' 
        else:
            for fc in dict_dict.keys():
                fc_keys = dict_dict[fc].keys()
                for k in fc_keys:
                    if p_type == k:
                        p_type_found = True
                        fc_where_found = fc.upper()
                        if 'CORE' in fc_where_found:
                            fc_object = 'CoreCategory'
                        elif 'DUCK' in fc_where_found:
                            fc_object = 'DuckCategory'
                        elif 'PROP' in fc_where_found:
                            fc_object = 'PropertyBundle'
                        else:
                            debug_print("Unknown class!\n")
                        check_type = 'NLG-Type'
        if p_type_found == False:
            check_type = 'Simple-Type'

        nlg.write(tab + 'if not isinstance(' + prop + ', Missing):' + '\n')


        if (is_list_type == False) and (card_field == 'noCardinality'):
            # DO IS INSTANCE CHECK WHICH CALLS XSD VALIDATOR HERE.
            pass



        if is_list_type == False:
            if check_type == 'CASE-Object':
                nlg.write(tab + tab + 'assert isinstance(' + prop + ', case.' + fc_object + '),\\' + '\n')
                nlg.write(tab + tab + '"[' + f_name + '] ' + prop + ' must be of type ' + fc_object + '."' + '\n')
                body_assert_types += 'REQUIRED    CASE    SINGLE    ' + prop + '\n'
            elif check_type == 'NLG-Type':
                nlg.write(tab + tab + 'assert (isinstance(' + prop + ', case.' + fc_object + ') and (' + prop + '.type=="' + p_type + '")),\\' + '\n')
                nlg.write(tab + tab + '"[' + f_name + '] ' + prop + ' must be of type ' + p_type + '."' + '\n')
                body_assert_types += 'REQUIRED    NLG     SINGLE    ' + prop + '\n'
            else:
                nlg.write(tab + tab + 'assert isinstance(' + prop + ', ' + p_type + '),\\' + '\n')
                nlg.write(tab + tab + '"[' + f_name + '] ' + prop + ' must be of type ' + p_type + '."' + '\n')
                body_assert_types += 'REQUIRED    NATIVE  SINGLE    ' + prop + '\n'

        else:
            nlg.write(tab + tab + 'assert isinstance(' + prop + ', list),\\' + '\n')
            nlg.write(tab + tab + '"[' + f_name + '] ' + prop + ' must be of type List of ' + p_type + '."' + '\n')
            if check_type == 'CASE-Object':
                nlg.write(tab + tab + 'assert all(isinstance(i, case.' + fc_object + ') for i in ' + prop + '),\\' + '\n')
                nlg.write(tab + tab + '"[' + f_name + '] ' + prop + ' must be of type List of ' + fc_object + '."' + '\n')
                body_assert_types += 'REQUIRED    CASE      LIST    ' + prop + '\n'
            elif check_type == 'NLG-Type':
                nlg.write(tab + tab + 'assert all(isinstance(i, case.' + fc_object + ')) and (i.type=="' + p_type + '") for i in ' + prop + '),\\' + '\n')
                nlg.write(tab + tab + '"[' + f_name + '] ' + prop + ' must be of type List of ' + p_type + '."' + '\n')
                body_assert_types += 'REQUIRED    NLG       LIST    ' + prop + '\n'
            else:
                nlg.write(tab + tab + 'assert all(isinstance(i, ' + p_type + ') for i in ' + prop + '),\\' + '\n')
                nlg.write(tab + tab + '"[' + f_name + '] ' + prop + ' must be of type List of ' + p_type + '."' + '\n')
                body_assert_types += 'REQUIRED    NATIVE    LIST    ' + prop + '\n'



        nlg.write(tab + 'else:\n')
        nlg.write(tab + tab + 'miss_prop_list.append(' + prop + ')' + '\n')
    return body_assert_types


#=====================================================
print "~~~ START"

#namespaces  = ['owl', 'core', 'olo']                        # Only these namespaces will be used.
namespaces  = ['http://unifiedcyberontology.org','http://case.example.org']
unknown_ns  = []
classes     = None
properties  = None
onto_dict   = {}
prop_dict   = {}
dict_dict   = {}
func_name   = None
prop_list   = []
card_dict   = None
line_number = 1
body_assert_types = ""
miss_prop_list = []
cust_prop_list = []
improper_turtl = []

# Load RDF via Ontospy.
graph = Ontospy(uri_or_path=input_file, rdf_format='turtle', verbose=True)
graph.load_rdf(input_file, verbose=True)
graph.extract_entities()


#=====================================================
# Copy stdout to a variable between (stdout -> copied_stdout -> stdout).

#print "-------------------------"
pointer_to_original_stdout = sys.stdout
sys.stdout = copied_stdout = StringIO()
graph.printClassTree()
classes    = graph.ontologyClassTree()
class_tree = copied_stdout.getvalue()
sys.stdout = pointer_to_original_stdout


#=====================================================
# Determine class name, nesting level, and parent (index=line # of printClassTree output).

c_tree_split = class_tree.split('\n')[:-1]
for uri in c_tree_split:
    if '----' in uri:
        space = uri.split('----')
        level = len(space) - 1
        last_nlg_type = nlg_type
    else:
        level = 0
    spltz = uri.split('----')[-1]
    if '#' in uri:
        namespace = spltz.split('#')[0]
        nlg_type  = spltz.split('#')[-1]
    elif ':' in uri:
        namespace = spltz.split(':')[0]
        nlg_type = spltz.split(':')[-1]
    else:                                                   #Skip unknown namespaces and add to list when syntax differs.
        namespace = spltz
        if namespace not in unknown_ns:
            unknown_ns.append(namespace)
        continue

    onto_dict[nlg_type] = {}
    onto_dict[nlg_type]['index'] = line_number
    onto_dict[nlg_type]['level'] = level
    if level == 0:
        onto_dict[nlg_type]['parent'] = 'root'
    elif ('----' in uri) and (onto_dict[last_nlg_type]['level'] >= level):
        count_down = line_number - 2
        while count_down != 0:
            for nlg_entry in onto_dict:
                comp_index = onto_dict[nlg_entry]['index']
                if comp_index == count_down:
                    comp_level = onto_dict[nlg_entry]['level']
                    if comp_level >= level:
                        count_down -= 1
                        break
                    else:
                        onto_dict[nlg_type]['parent'] = nlg_entry
                        count_down = 0
                        break
    else:
        onto_dict[nlg_type]['parent'] = last_nlg_type
    line_number += 1

#=====================================================
# Also avoid standard output while still piping the PropertyTree into a variable.

pointer_to_original_stdout = sys.stdout
sys.stdout = copied_stdout = StringIO()
graph.printPropertyTree()
properties  = graph.ontologyPropTree()
property_tree = copied_stdout.getvalue()
sys.stdout = pointer_to_original_stdout


#=====================================================
# Get the properties for each class.
# Also correct parent for level==0 classes that have subClassOf.

for ontoclass_obj in classes:
    class_list = classes[ontoclass_obj]
    for c in class_list:
        if '#' in str(c):
            class_split = str(c).split('#')
            nlg_type    = class_split[1].strip('*>')
        elif ':' in str(c):
            class_split = str(c).split(':')
            nlg_type    = class_split[1].strip('*>')
        else:                                               #Skip unknown namespaces and add to list when syntax differs.
            spltz     = str(c).strip('<Class ').strip('>').strip('*')
            namespace = spltz
            if namespace not in unknown_ns:
                unknown_ns.append(namespace)
            continue

#        print nlg_type                                      #TEST1
#        print c.domain_of                                   #Use these to see inheritance details.
#        print c.range_of
#        print c.domain_of_inferred
#        print c.range_of_inferred

        prop_list = []
        if c.domain_of == []:                               #Classes with no domain (properties) are included to allow for children with properties (these children need may need a parent to retain the correct nesting level and linkage back to their root parent).
            debug_print("Gap or ambiguity/redundancy in ontology (no properties for class):\n{}".format(c))
        for uri in c.domain_of:
            if '#' in str(uri):
                property_split = str(uri).split('#')
                property_type  = property_split[1].strip('*>')
            elif ':' in str(uri):
                property_split = str(uri).split(':')
                property_type  = property_split[1].strip('*>')
            else:
                spltz     = str(uri).strip('<Property ').strip('>').strip('*')
                namespace = spltz
                if namespace not in unknown_ns:
                    unknown_ns.append(namespace)
                continue
            prop_list.append(property_type)
        onto_dict[nlg_type]['properties'] = prop_list

        if onto_dict[nlg_type]['level']==0:                 #This only handles single parents.
            parent_list = graph.sparqlHelper.getClassDirectSupers(c.uri)
            for embedded_tuple in parent_list:
                for parent_uri in embedded_tuple:
                    if '#' in str(parent_uri):
                        parent_split   = str(parent_uri).split('#')
                        parent_type    = parent_split[1].strip('*>')
                        onto_dict[nlg_type]['parent'] = parent_type
                    elif ':' in str(parent_uri):
                        parent_split   = str(parent_uri).split(':')
                        parent_type    = parent_split[1].strip('*>')
                        onto_dict[nlg_type]['parent'] = parent_type
                    else:
                        spltz     = str(parent_uri).strip('<Class ').strip('>').strip('*')
                        namespace = spltz
                        if namespace not in unknown_ns:
                            unknown_ns.append(namespace)
                        continue


#=====================================================
# Create properties dictionary to track their types.

for ontoprop_obj in properties:
    prop_list = properties[ontoprop_obj]
    for p in prop_list:
        if '#' in str(p):
            prop_split = str(p).split('#')
        elif ':' in str(p):
            prop_split = str(p).split(':')
        else:                                               #Skip unknown namespaces and add to list when syntax differs.
            spltz     = str(p).strip('<Property ').strip('>').strip('*')
            namespace = spltz
            unknown_ns.append(namespace)
            continue
        prop       = prop_split[1].strip('*>')
        possible_prop_types = p.ranges

        prop_types = []
        for ppt in possible_prop_types:
            if '#' in str(ppt):
                ppt_split = str(ppt).split('#')
                ppt_type  = ppt_split[1].strip('*>')
            elif ':' in str(ppt):
                ppt_split = str(ppt).split(':')
                ppt_type  = ppt_split[1].strip('*>')
            else:
                spltz     = str(ppt).strip('<Property ').strip('>').strip('*')
                namespace = spltz
                unknown_ns.append(namespace)
                continue
            prop_types.append(ppt_type) 

        if prop_types == []:                                #Remove properties with no possible types.
            debug_print("Gap or ambiguity/redundancy in ontology (property has no possible types):\n{}".format(prop))
            onto_prop_list = onto_dict[nlg_type]['properties']
            for op in onto_prop_list:
                if prop == op:
                    prop_index = onto_prop_list.index(op)
                    del onto_dict[nlg_type]['properties'][prop_index]
                    break
            continue
        prop_dict[prop] = prop_types



#=====================================================
# Determine function name based on nesting level and parent's function name.
# First level zero must be determined first so that sub names can be based on their parent's name.
# If parent was not parsed in the class tree, skip it (reported because this means top-level item
# does not have parent specified in Turtle) and relabel parent to 'root' and rerun (so that children
# can still be processed).

#print "-------------------------"
count = 1
while count < (line_number + 1):
    for current_entry in onto_dict:
        index = onto_dict[current_entry]['index']
        if index == count:
            nlg_type = current_entry
            break
    level = onto_dict[nlg_type]['level']
    parent = onto_dict[nlg_type]['parent']

    if (parent == 'root'):              
        func_name = 'duck_'
        onto_dict[nlg_type]['func_name'] = func_name
        count += 1
    elif (parent == 'UcoObject'):
        if not (level == 0 or level == 1):
            print "Error in ontology! UcoObject can only be the parent of a class with nesting level of zero (top-level) or one (below top-level)."
        func_name = 'core_'
        onto_dict[nlg_type]['func_name'] = func_name
        count += 1
    elif (parent == 'PropertyBundle'):
        if not (level == 0 or level == 1):
            print "Error in ontology! PropertyBundle can only be the parent of a class with nesting level of zero (top-level) or one (below top-level)."
        func_name = 'prop_'
        onto_dict[nlg_type]['func_name'] = func_name
        count += 1
    elif (parent not in onto_dict.keys()):
        debug_print("Gap or ambiguity/redundancy in ontology (parent class does not exist in the class tree):\n{}".format(parent))
        onto_dict[nlg_type]['parent'] = 'root'
        continue
    else:
        parent_func_name = onto_dict[parent]['func_name']
        func_name = parent_func_name + 'sub_'
        onto_dict[nlg_type]['func_name'] = func_name
        count += 1


#=====================================================
# Sort onto_dict entries, resulting in dict_dict (alphabetical and categorical).

for k in onto_dict.keys():
    func_category = onto_dict[k]['func_name']
    if func_category not in dict_dict.keys():
        dict_dict[func_category] = {}
    dict_dict[func_category][k] = onto_dict[k]


#=====================================================
# Parse input_file

restrx      = parse_restrictions.Restrictions(input_file, namespaces, onto_dict.keys(), prop_dict.keys())
card_dict   = restrx.parse(cardinality=True)
del onto_dict                                               #Free memory.


#=====================================================
# Use the class/property information gathered above to write the Python API functions in NLG.py.
# All statements represented here can be found in NLG_template.txt in the CASE-Python-API repository.

nlg = open('outputs/new_NLG.py','w')
ver = '0.1.0'   #Change version of NLG here to reflect ontology version number.

nlg.write('# CASE NLG VERIFIER v' + ver)
nlg_prefix = open('inputs/header.txt','r')
nlg_header = nlg_prefix.read()
nlg.write(nlg_header)
nlg_prefix.close()

for func_category in sorted(dict_dict):
    category = func_category.upper().replace('_',' ')[:-1]
    nlg.write("\n\n#=====================================================\n")
    nlg.write("#-- {}\n\n".format(category))

    case_class = None
    if 'SUB' in category:
        case_class = 'SUB'
    elif 'DUCK' in category:
        case_class = 'DUCK'
    elif 'CORE' in category:
        case_class = 'CORE'
    elif 'PROP' in category:
        case_class = 'PROP'
    else:
        debug_print("Improper use of ontology! (unknown CASE Python class):\n{}\n".format(func_category))
        debug_print("If the new NLG items have a new ontological (relationship) structure\
                     from the other classes consider making a new class in case.py.\nThis\
                     is not advised however.")
        continue

    for nlg_type in sorted(dict_dict[func_category]):
        c_list     = dict_dict[func_category].keys()
        f_name     = dict_dict[func_category][nlg_type]['func_name'] + nlg_type
        parent     = dict_dict[func_category][nlg_type]['parent']
        p_list     = sorted(dict_dict[func_category][nlg_type]['properties'])
        num_props  = len(p_list)
        tab        = '\t'

        if nlg_type in card_dict.keys():
            prop_card_dict = card_dict[nlg_type]
        else:
            prop_card_dict = None


        #=====================================================
        # DEFINITION

        nlg.write('def ' + f_name + '(')
        if case_class == 'SUB':
            nlg.write('case_doc, parent_object')
        elif (case_class == 'DUCK') or (case_class == 'CORE'):
            nlg.write('case_doc')
        elif case_class == 'PROP':
            nlg.write('core_object')
        else:
            debug_print("ERROR (unknown case_class):\n{}".format(case_class))
        i = 1
        if num_props > 0:
            nlg.write(', ')
            for prop in p_list:
                nlg.write(prop + '=Missing()')
                if i != num_props:
                    nlg.write(', ')
                i += 1
        nlg.write("):\n")


        #=====================================================
        # DOCSTRINGS

        nlg.write(tab + "'''\n")

# USE DEBUG_PRINT STATEMENTS HERE RATHER THAN BODY ASSERTS (for same block of code).
        for prop in p_list:
            card_stuff = None
            card_phrase = None
            if prop in prop_card_dict.keys():
                card_stuff = prop_card_dict[prop]
                card_field = card_stuff['card-field']
                card_type  = card_stuff['card-type']
                card_value = card_stuff['card-value']
            else:
                card_field = 'noCardinality'
                card_type  = 'string'
                card_value = 'any'

            if card_field == 'minQualifiedCardinality':
                card_phrase = 'At least '
                card_phrase += card_value + ' '
                card_phrase += 'of type '
            elif card_field == 'qualifiedCardinality':
                card_phrase = 'Exactly '
                card_phrase += card_value + ' '
                card_phrase += 'of type '
            elif card_field == 'maxQualifiedCardinality':
                card_phrase = 'At most '
                card_phrase += card_value + ' '
                card_phrase += 'of type '
            elif card_field == 'noCardinality':
                card_phrase = 'Any number of type '
            else:
                debug_print("Cardinality issue with property{}\n".format(prop))

            prop_types = prop_dict[prop]
            if len(prop_types) > 1:
                debug_print("Property ({}) has multiple types specified:\n{}\n".format(prop, prop_types))
                continue
            else:
                p_type = prop_types[0]
                card_phrase += p_type + '.\n'
                nlg.write(tab + ':param ' + prop + ': ')
                nlg.write(card_phrase)

        if case_class == 'SUB':
            nlg.write(tab + ':return: A SubCategory object.\n')
        elif case_class == 'DUCK':
            nlg.write(tab + ':return: A DuckCategory object.\n')
        elif case_class == 'CORE':
            nlg.write(tab + ':return: A CoreCategory object.\n')
        elif case_class == 'PROP':
            nlg.write(tab + ':return: A PropertyBundle object.\n')
        nlg.write(tab + "'''\n\n")


        #=====================================================
        # BODY ASSERTS FOR PARENT OBJECTS

        if case_class == 'SUB':
            if 'DUCK' in category:
                nlg.write(tab + "assert (isinstance(parent_object, case.DuckCategory) and parent_object.type=='" + parent + "'))," + '\\' + '\n')
                nlg.write(tab + '"[' + f_name + '] parent_object must be of type ' + parent + '."\n\n')
            elif 'CORE' in category:
                nlg.write(tab + "assert (isinstance(parent_object, case.CoreCategory) and parent_object.type=='" + parent + "'))," + '\\' + '\n')
                nlg.write(tab + '"[' + f_name + '] parent_object must be of type ' + parent + '."\n\n')
            elif 'PROP' in category:
                nlg.write(tab + "assert (isinstance(parent_object, case.PropertyBundle) and parent_object.type=='" + parent + "'))," + '\\' + '\n')
                nlg.write(tab + '"[' + f_name + '] parent_object must be of type ' + parent + '."\n\n')
            else:
                debug_print("ERROR (unknown category/Python class):\n{}".format(category))


        #=====================================================
        # BODY ASSERTS FOR REQUIRED PARAMETERS

        # The following is assumed: a cardinality field exists for any type of restriction. Otherwise, 'any number of' is assumed (0-N).
        # It is also assumed that only one cardinality field can exist per property.
        # minQualifiedCardinality   = at least X    = 1/N to M      = REQUIRED
        # qualifiedCardinality      = exactly X     = 1/N           = REQUIRED
        # qualifiedCardinality      = exactly X     = 0             = OPPOSITE OF REQUIRED (not handled - exceptional/rarely used)
        # maxQualifiedCardinality   = at most X     = 0 to 1/N      = OPTIONAL
        # no cardinality field      = any number X  = 0 to M        = OPTIONAL

        for prop in p_list:
            p_required = None
            card_stuff = None
            is_list_type = None
            is_meta_type = None
            if prop in prop_card_dict.keys():
                card_stuff = prop_card_dict[prop]
                card_field = card_stuff['card-field']
                card_type  = card_stuff['card-type']
                card_value = card_stuff['card-value']

                if card_field == 'minQualifiedCardinality':
                    p_required = True
                    is_list_type = True
                elif ((card_field == 'qualifiedCardinality') and (int(card_value) != 0)):
                    p_required = True
                    is_list_type = False
                elif ((card_field == 'qualifiedCardinality') and (int(card_value) > 1 )):
                    p_required = True
                    is_list_type = True
                else:
                    p_required = False
                    is_list_type = True

            if p_required == True:
                nlg.write(tab + 'assert not isinstance(' + prop + ', Missing),\\' + '\n')
                nlg.write(tab + '"[' + f_name + '] ' + prop + ' is required."' + '\n')
                bat = write_body_assert(prop, p_required, prop_dict, dict_dict, card_field, card_type, card_value, is_list_type, tab, f_name,  body_assert_types)
                body_assert_types += bat
            else:
                # Skip optional parameters.
                # These are added in the next block (copy of this block but with p_required == False.
                continue


        #=====================================================
        # BODY ASSERTS FOR OPTIONAL PARAMETERS

        nlg.write('\n\n')

        for prop in p_list:
            p_required = None
            card_stuff = None
            is_list_type = None
            is_meta_type = None
            if prop in prop_card_dict.keys():
                card_stuff = prop_card_dict[prop]
                card_field = card_stuff['card-field']
                card_type  = card_stuff['card-type']
                card_value = card_stuff['card-value']
            else:
                card_field = 'noCardinality'
                card_type  = 'string'
                card_value = 'any'

            if card_field == 'minQualifiedCardinality':
                p_required = True
                is_list_type = True
            elif ((card_field == 'qualifiedCardinality') and (int(card_value) != 0)):
                p_required = True
                is_list_type = False
            elif ((card_field == 'qualifiedCardinality') and (int(card_value) > 1 )):
                p_required = True
                is_list_type = True
            elif card_field == 'noCardinality':
                p_required = False
                is_list_type = None
            else:
                debug_print("Error with cardinality for property:\n{}\n".format(prop))

                if p_required == False:
                    bat = write_body_assert(prop, p_required, prop_dict, dict_dict, card_field, card_type, card_value, is_list_type, tab, f_name,  body_assert_types)
                    body_assert_types += bat
                else:
                    # Skip required parameters.
                    # Already written.
                    continue


        #=====================================================
        # RETURN
        if case_class == 'SUB':
            nlg.write(tab + "return case_doc.create_SubCategory('" + nlg_type + "'")
        elif case_class == 'DUCK':
            nlg.write(tab + "return case_doc.create_DuckCategory('" + nlg_type + "'")
        elif case_class == 'CORE':
            nlg.write(tab + "return case_doc.create_CoreCategory('" + nlg_type + "'")
        elif case_class == 'PROP':
            nlg.write(tab + "return case_doc.create_PropertyBundle('" + nlg_type + "'")
        i = 1
        if num_props > 0:
            nlg.write(', ')
            for prop in p_list:
                nlg.write(prop + '=' + prop)
                if i != num_props:
                    nlg.write(', ')
                i += 1
        nlg.write(")")
        nlg.write('\n\n')
nlg.close()


#=====================================================
# DEBUGGING (PYTHON-API AND CASE ONTOLOGY)
print "-------------------------"
print "TESTING PRINTS\n"

#pp.pprint(onto_dict)
#print ""
#pp.pprint(prop_dict)
#print ""
#pp.pprint(dict_dict)
#print ""
#pp.pprint(card_dict)
#print ""
#print(body_assert_types)
#print ""

print "-------------------------"
print "ONTOSPY  TREES\n"

#print class_tree
#print ""
#print property_tree
#print ""

print "-------------------------"
print "DEBUG WARNINGS\n"
debug_print("Unknown namespaces:\n{}".format(unknown_ns))

debug_txt.close()
print "~~~ END"
