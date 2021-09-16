from newpub import on_connect
import paho.mqtt.client as paho  # mqtt library
import os
import json
import time
from datetime import datetime


def on_publish(client, userdata, result):  # create function for callback
    print("published data is : ")
    pass


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('connected OK')
    else:
        print('Bad connection Returned code=', rc)


# host name is localhost because both broker and python are Running on same
# machine/Computer.
# host name , Replace with your IP address.
broker = "localhost"
topic = "house/sensor1"  # topic name
port = 1883  # MQTT data listening port
ACCESS_TOKEN = 'M7OFDCmemyKoi461BJ4j'  # not manditory


client1 = paho.Client("control1")  # create client object
client1.on_publish = on_publish  # assign function to callback
# client1.username_pw_set('mn', '123')  # access token from thingsboard device
client1.connect(broker)  # establishing connection
client1.on_connect = on_connect
# publishing after every 5 secs
while True:
    payload = 't'
    '''    payload = "{"
    payload += "\"Temperature\":10"
    payload += ","
    payload += "\"Humidity\":50"
    payload += "}"'''
    ret = client1.publish(topic, payload)  # topic name is test
    print(payload)
    print("Please check data on your Subscriber Code \n")
    time.sleep(5)
#mosquitto - c / etc/mosquitto/mosquitto.conf
