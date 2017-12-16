from nanpy import (ArduinoApi, SerialManager)
import requests
from time import sleep

try:
    connection = SerialManager()
    a = ArduinoApi(connection = connection)
except:
    print('Failed to connect to Arduino.')

ldrPin = 0
a.pinMode(ldrPin, a.INPUT)

while True:
    ldrStatus = a.analogRead(ldrPin)
    if ldrStatus >= 300:
        requests.post('https://api.simplepush.io/send', data={'key':'Q4bcip', 'title': 'Washroom Lights', 'msg': 'The washroom lights are on!'})
    else:
        pass
    sleep(120)
