import subprocess
import os
from lxml import etree
from StringIO import StringIO

class XSDValidator():
    def __init__(self, xsd_file, prop_dict=None):
        self.xsd_file = xsd_file
        self.prop_dict = prop_dict

    def generate_xsd_file(self):
        xsd_restrictions = []

        for key in self.prop_dict.keys():  # the way i am appending to from prop_dict to get xsd keys
            data = '<xsd:element name=\"{0}\" type="xsd:{1}"/>'.format(key, self.prop_dict.get(key, None)[0])
            xsd_restrictions.append(data)

        string = StringIO('''<?xml version="1.0" encoding="UTF-8" ?>\n<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">\n\t'''
                          + '\n\t'.join(xsd_restrictions) + '\n</xsd:schema>')

        with open(self.xsd_file, 'w') as f:
            f.write(string.getvalue())

    def remove_non_xsd_types(self):
        """
        Uses XSD 1.1 compliant types and removes all other types (xsd11-validator.jar).
        Removes CASE types.
        """
        is_valid = False
        while not is_valid:
            err_line = self.find_xsd_errs()
            if err_line == -1:
                break
            with open(self.xsd_file, 'r+') as xs:
                data = xs.readlines()
                # print(data)
                del data[err_line - 1]  # delete invalid line
                xs.seek(0)
                for i in data:
                    xs.write(i)
                xs.truncate()

    def find_xsd_errs(self):
        # print(os.getcwd())
        args = ['java', '-jar', os.getcwd() + '/inputs/xsd11-validator.jar',
                '-sf', self.xsd_file, '-if', 'n']
        data, _ = get_proc(args)

        data = data.decode('utf-8')
        # print(data)
        if '[Error]' in data:
            line_num = data.split(':')[2]
            print('removing line: {0} from {1}'.format(
                line_num, self.xsd_file))
            return int(line_num)
        else:
            print('valid format')
        return -1

    def validateXSD(cls, element_value, element_name, xsd_file):
        element = etree.Element(element_name)

        element.text = str(element_value)
        temp_xml = 'temp.xml'
        with open(temp_xml, 'wb') as f:
            f.write(etree.tostring(element))

        args = ['java', '-jar', 'xsd11-validator.jar',
                '-sf', xsd_file, '-if', temp_xml]

        stderr, stdout = get_proc(args)

        stderr, stdout = stderr.decode('utf-8'), stdout.decode('utf-8')
        if '[Error]' in stderr:
            print(stderr)
            return False
        return True


def get_proc(args):
    proc = subprocess.Popen(
        args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    return stderr, stdout
