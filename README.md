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

```python
import os
import json
from json2xml import json2xml
from json2xml.utils import readfromstring
from cryptography.fernet import Fernet
import flask
from flask import request, jsonify
```
and for cont_b:

```python
import requests
from cryptography.fernet import Fernet
```

then run the cont_a.py and it will create the endpoint via Flask with encrypted content and localhost:5000/files. Also it will generate 'secret.key' file. You need to upload it to the cont_b directory and then run:

```bash
>python cont_b.py
```
## Result
It will generate the files with original names with XML extension. 

## License
[MIT](https://choosealicense.com/licenses/mit/)