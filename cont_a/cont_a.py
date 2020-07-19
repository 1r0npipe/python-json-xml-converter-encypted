import os
import json
from json2xml import json2xml
from json2xml.utils import readfromstring
from cryptography.fernet import Fernet
import flask
from flask import request, jsonify

xml_content = dict()
xml_content_arr = []
count_files = 0

if __name__ == "__main__":
    web_app = flask.Flask(__name__)
    web_app.config['DEBUG'] = True

    key = os.getenv('KEY_ENCRYPT')
    key = Fernet.generate_key()
    with open("/shared/secret.key", "wb") as key_file:
        key_file.write(key)

    try:
        # reading the content of file
        json_files = open('json_list.txt', 'r')
        fernet = Fernet(key)
        for file_json in json_files.readlines():
            if not file_json.startswith("#"):
                try:
                    opened_json = open(file_json.strip())
                    json_out = str(json.load(opened_json)).replace('\'', '\"')
                    data = readfromstring(json_out)
                    xml_out = json2xml.Json2xml(data, wrapper="all", pretty=True, attr_type=False).to_xml()
                    xml_out_encode = xml_out.encode()
                    xml_encrypted = fernet.encrypt(xml_out_encode)
                    xml_content['id'] = str(count_files)
                    xml_content['file'] = str(xml_encrypted)
                    xml_content['filename'] = file_json.strip().replace('json','xml')
                    xml_content_arr.append(xml_content.copy())
                    count_files = count_files + 1
                except:
                    print("File - " + file_json + " cannot be opened")
                    exit()
                finally:
                    #xml_file.close()
                    opened_json.close()

    except:
        print("The list or JSON file cannot be opened or something goes worng, please check the file format/permissions")
        exit()
    finally:
        json_files.close()

    @web_app.route('/files', methods=['GET'])
    def file_id():
        json_output = xml_content_arr
        return jsonify(json_output)

    web_app.run(host='0.0.0.0')

