import time
import paho.mqtt.client as mqtt_client
import random
from statistics import mean
import serial

lst = []
ser = serial.Serial("COM6", timeout=1)
min = 100
max = 0

def on_message(client, userdata, message):
    global max
    global min
    data = message.payload
    topic = message.topic
    print(f"Received message on {topic}: {data}; min: {min}, max: {max}")
    if topic == "dz/hava/image/photo/max":
        max = int(data)

    if topic == "dz/hava/image/min":
        min = int(data)

    if topic == "dz/hava/image/stream":
        if int(data) < (min + max) / 2:
            ser.write(bytearray([ord('1')]))
        else:
            ser.write(bytearray([ord('0')]))

broker = "broker.emqx.io"

client = mqtt_client.Client(f'lab_{random.randint(10000, 99999)}')
client.on_message = on_message

try:
    client.connect(broker)
except Exception:
    print('Failed to connect. Check network')
    exit()

client.loop_start()

print('Subscribing')
client.subscribe("dz/hava/image/stream")
client.subscribe("dz/hava/image/min")
client.subscribe("dz/hava/image/max")
time.sleep(600)
client.disconnect()
client.loop_stop()
print('Stop communication')