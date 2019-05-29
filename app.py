from bottle import route, run, template
import requests
import datetime
import xml.etree.ElementTree as ET
from json import dumps

@route('/api/rate/<code:re:[A-Z]{3}>')
@route('/api/rate/<code:re:[A-Z]{3}>/<year:re:\d{4}>-<month:re:\d{2}>-<day:re:\d{2}>')
def rate(code, year='', month='', day=''):
    if not year:
        date = datetime.date.today() + datetime.timedelta(days=1)
        year = date.strftime('%Y')
        month = date.strftime('%m')
        day = date.strftime('%d')

    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp?date_req={dd}/{mm}/{yyyy}".format(dd=day,mm=month,yyyy=year))
    root = ET.fromstring(response.content)
    for value in root.findall('Valute'):
        if value.find('CharCode').text == code:
            rate = value.find('Value').text
            break
    if rate:
        return dumps({"code": code, "rate": rate, "date": "{yyyy}-{mm}-{dd}".format(dd=day,mm=month,yyyy=year)})
    return ''

run(host='0.0.0.0', port=8080)
