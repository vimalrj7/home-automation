from nanpy import (ArduinoApi, SerialManager)
from time import sleep
import sys

# Connect Pi to the Arduino
try:
    connection = SerialManager()
    a = ArduinoApi(connection = connection)
except:
    print("Failed to connect")

# Setup
comm = sys.argv[1]
relayPin = 7
a.pinMode(relayPin, a.OUTPUT)

# Use Tasker to send a SSH command to turn lamp on/off
if comm == 'on':
    a.digitalWrite(relayPin, a.LOW)
    print('Lamp is on!')
else:
    a.digitalWrite(relayPin, a.HIGH)
    print('Lamp is off!')
