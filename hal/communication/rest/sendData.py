import urllib

import requests
import time


def sendData(sensor_name, sensor_value):
    """
    Invio dei dati provenienti dai sensori al SVO

    """

    try:
        f = open('reg.dat', 'r')
        key = f.readline()

    except IOError:
        print ("reg.dat file not found")

    payload = {'name': sensor_name,
               'type': 'number',
               'value': sensor_value,
               'regId': key,
               'timestamp': time.time()
               }

    param = urllib.urlencode(payload)
    url = "http://lysis-78.appspot.com/sendData"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache"
    }

    r = requests.request("POST", url=url, data=param,
                         headers=headers)
    print(r.text)
    print (r.status_code)

