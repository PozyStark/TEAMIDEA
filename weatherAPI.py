
import json
import xml.etree.ElementTree as ET
import requests

jup_code = 'JPY'


def get_struct(code):
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    data = response.text
    data = data.replace('<', '\n')
    data = data.replace('>', ' ')
    data = data.split('\n')
    get_value = False
    struct = ''
    for val in data:
        if val == f'CharCode {code}':
            get_value = True
            # print(val)
        if get_value and val.find('/'):
            struct += val + '\n'
    return struct


s = get_struct(jup_code).split('\n')
print(s)




