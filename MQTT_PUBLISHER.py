import paho.mqtt.client as paho  # mqtt library
import time

# host name , Replace with your IP address.
broker = "Host Name"
topic = "topic"  # topic name
port = 1883  # MQTT data listening port


def on_publish(client, userdata, result):  # create function for callback
    print("published data is : ")
    pass


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('connected OK')
    else:
        print('Bad connection Returned code=', rc)


def on_message(client, userdata, message):
    print("received data is :")
    print(str(message.payload.decode("utf-8")))  # printing Received message
    print("")


client1 = paho.Client("control1")  # create client object
client1.on_publish = on_publish  # assign function to callback
client1.connect(broker, port, keepalive=60)  # establishing connection
client1.on_message = on_message
client1.on_connect = on_connect
# publishing after every 5 secs
while True:
    print('data to be communicated')
    payload = 'Hello'
    ret = client1.publish(topic, payload)  # topic name is test
    print(payload)
    print('_________________')
    time.sleep(5)
