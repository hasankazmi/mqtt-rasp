import paho_mqtt_client as mqtt

def onconnect(client, userdata, flags, rc):
    print("connected" + str(rc))

    client.subscribe("code collection/test")
    client.subscribe("code collection/topic")

def onmessage(client, userdata, msg):
    print(msg.topic + "" + str(msg.payload))

    if msg.payload == "hello":
        print("recieve msg")
    
    if msg.payload == "world":
        print("recive msg 1")

client = mqtt.client
client.onmessage = onmessage
client.onconnect = onconnect

client.connect("test.mosquito.com", 1866, 60)

client.loop_forever()