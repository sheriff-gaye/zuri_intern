import csv
import xml.etree.cElementTree as ET

root = ET.Element("root")
doc = ET.SubElement(root, "input")

with open('hello2.sda') as f:
    csv_reader = csv.reader(f, delimiter='|')
    for row in csv_reader:
        blanks_removed_row = ' '.join(row).split()
        input = ET.SubElement(doc, "item")
        for i, item in enumerate(blanks_removed_row, start=1):
            ET.SubElement(input, "data{0}".format(i)).text = item

tree = ET.ElementTree(root)
tree.write("filename.xml", encoding='utf-8', xml_declaration=True)  # save tree
