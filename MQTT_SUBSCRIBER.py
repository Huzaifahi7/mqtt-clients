import paho.mqtt.client as paho
# host name , Replace with your IP address.
broker = "Host Name"
topic = "topic"  # topic name


def on_message(client, userdata, message):
    print("received data is :", str(message.payload.decode("utf-8")))
    print('_____')


client = paho.Client("user",)  # create client object

print("connecting to broker host", broker)
client.connect(broker)  # connection establishment with broker
print("subscribing begins here")
client.subscribe(topic)  # subscribe topic test

client.on_message = on_message

client.loop_forever()
