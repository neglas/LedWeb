import paho.mqtt.client as mqtt
import subprocess

def on_connect(client, userdata, flags, rc):
    print("Connected to broker.")
    client.subscribe("home/sensors/buttons")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"Recieved on {msg.topic}: {payload}")

    if payload == "triggered":
        print("recieved triggered")
        subprocess.call(['sh', '/home/neglas/Webapp/TurnLightsOn.sh'])

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()
