# Exporter Json-XML via encyrption


# python-json-xml-converter-encypted
Container A should convert input json to xml, encrypt and transfer to cont. B and output of XML

# JSON-XML-TRANSFER with encryption

When you run script from cont_a - cont_a.py it will encrypt all json files which will be provided as a list at and generate secret.key file, which will be then required to copy to directory with script as cont_b.py and then run python cont_b.py it will generate the files which will be listed 

## Filling the file

make a file at the cont_a directory with list of JSON files might be required to transfer to XML with encryption, '#' can be used to comment the line

```bash
cont_a\json_list.txt
```

## Usage
Those imports are required for cont_a:

## Some pre-requisits:
Make volume available first:
```bash
sudo docker volume create --driver local \
    --opt type=none \
    --opt device=/home/something/share \
    --opt o=bind shared
```
make sure you have all requered imorts for container A (cont_a.py)
```python
import os
import json
from json2xml import json2xml
from json2xml.utils import readfromstring
from cryptography.fernet import Fernet
import flask
from flask import request, jsonify
```
and for container B (cont_b.py):

```python
import requests
from cryptography.fernet import Fernet
```

## Using docker-composer
You need to make sure you have docker composer installed, and run at the project direcotry:
```bash
# sudo docker-compose build
```
it should build the environment for you, then run:
```bash
# sudo docker-compose up
```
it will leave cont_a up and running under Flask and cont_b should perform the getting of the encrypted content from A and make files as the attached direcotry with XML format.

## Result
It will generate the files with original names with XML extension. 

## License
[MIT](https://choosealicense.com/licenses/mit/)