from lxml import etree
from io import StringIO
import sys

filename_xml = sys.argv[1]

# open and read xml file
with open(filename_xml, 'r') as xml_file:
    xml_to_check = xml_file.read()

# parse xml
try:
    doc = etree.parse(StringIO(xml_to_check))
    print('Le document XML est bien formé !')

# check for file IO error
except IOError:
    print("Le document XML n'est pas bien formé !")