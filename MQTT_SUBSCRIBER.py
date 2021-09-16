import paho.mqtt.client as paho
import time
import sys
import datetime
import time
broker = "mqttdns.eastus.cloudapp.azure.com"  # host name
topic = "tests"


def messages(client, userdata, message):
    print("received data is :")
    print(str(message.payload.decode("utf-8")))  # printing Received message
    print("")


def subscribe(client, userdata, mid, granted_qos):
    print("subscribed")


client = paho.Client("user")  # create client object
client.on_message = messages
client.username_pw_set('mn', '123')
print("connecting to broker host", broker)
client.connect(broker, 1883)  # connection establishment with broker
# subscribe topic test
client.subscribe(topic)
client.on_subscribe = subscribe
print("subscribing begins here")

while True:
    print('s')
    
    client.loop_forever()  # contineously checking for message
    # time.sleep(5)
