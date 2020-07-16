#import os
import requests
from cryptography.fernet import Fernet

#TOKEN = os.getenv('KEY_TOKEN')
URL_FILES = 'http://conta:5000/files'
URL_NUMBER = 'http://conta:5000/numbers'
SUCCESS_CODE = 200
data_array = []

def upload_key():
    return open("/shared/secret.key", "rb").read()

if __name__ == "__main__":

    try:
        request_files = requests.get(URL_FILES)
        if request_files.status_code == SUCCESS_CODE:
            data_array = request_files.json()
        else:
            print("Bad request, no data migt be getting from the remote host(cont_a)")
    except:
        print("Something goes wrong with remote connection, dropped...")
        exit()

    key = upload_key()
    fernet_ = Fernet(key)

    
    for xml_file in data_array:
        file_xml = open('/shared/' + xml_file['filename'],'w')
        xml_file = bytes(xml_file['file'][2:len(xml_file['file'])-1], encoding='utf-8')
        decrypted_message = fernet_.decrypt(xml_file)
        file_xml.write(decrypted_message.decode())
        file_xml.close()
        

    #num_files = requests.get(URL_NUMBER)
    #if num_files.status_code == SUCCESS_CODE:
    #        num_files = num_files.json()
    #        print(num_files[1])