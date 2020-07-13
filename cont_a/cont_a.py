import os
import requests
import cryptography
import json
from json2xml import json2xml
from json2xml.utils import readfromstring

KEY = os.getenv('KEY_ENCRYPT')

# reading the content of file
try:
    json_files = open('json_list.txt', 'r')
    i = 1 # count number of xml files
    for file_json in json_files.readlines():
        if not file_json.startswith("#"):
            try:
                #path = os.path.join(os.path.dirname(os.path.realpath('__file__')), file_json)
                opened_json = open(file_json.strip())
                json_out = str(json.load(opened_json)).replace('\'', '\"')
                data = readfromstring(json_out)
                xml_out = json2xml.Json2xml(data, wrapper="all", pretty=True, attr_type=False).to_xml()
                xml_file = open('file' + str(i) + '.xml', 'w')
                xml_file.write(xml_out)
                i = i + 1
            except:
                print("File - " + file_json + " cannot be opened")
                exit()
            finally:
                xml_file.close()
                opened_json.close()

except:
    print("The list or JSON file cannot be opened or something goes worng, please check the file format/permissions")
    exit()
finally:
    json_files.close()
