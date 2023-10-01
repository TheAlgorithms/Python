import json
import xmltodict


def json_to_xml(json_data, pretty=True):
    xml_data = xmltodict.unparse(json_data, pretty=pretty)
    return xml_data


# Load the JSON data
with open("myjson.json", "r") as in_file:
    json_data = json.load(in_file)

# Convert the JSON data to XML
xml_data = json_to_xml(json_data)

# Save the XML data to a file
with open("myxml.xml", "w") as out_file:
    out_file.write(xml_data)
