
import xml.dom.minidom
import urllib.request
from math import *

country_code = 'JPY'

response = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp")

doc = xml.dom.minidom.parse(response)

node = doc.documentElement

valute = node.getElementsByTagName('Valute')


def get_text(nodelist):
    rc = ""
    for n in nodelist:
        if n.nodeType == n.TEXT_NODE:
            rc = rc + n.data
    return rc


for v in valute:
    code = v.getElementsByTagName('CharCode')[0].childNodes  # Код страны
    nominal = v.getElementsByTagName('Nominal')[0].childNodes  # Номинал
    value = v.getElementsByTagName('Value')[0].childNodes  # Значение валюты

    f_value = float(get_text(value).replace(',', '.'))
    i_nominal = int(get_text(nominal))

    if get_text(code) == country_code:
        print(f'Code:{get_text(code)} Nominal:{get_text(nominal)} Value:{get_text(value)}')
        print(f'1 RUB = {round(f_value / i_nominal, 3)} JPY')



