import time
import paho.mqtt.client as mqtt_client
import random
from statistics import mean
import serial

lst = []
ser = serial.Serial("COM6", timeout=1)

def on_message(client, userdata, message):
    data = str(message.payload.decode("utf-8"))
    topic = str(message.topic.encode("utf-8"))
    print(f"Received message on {topic}: {data}")
    lst.append(int(data))
    if len(lst) > 100:
        lst.pop(0)
        if mean(lst[:50]) > mean(lst[50:]):
            ser.write(bytearray([ord('1')]))
        else:
            ser.write(bytearray([ord('0')]))

broker = "broker.emqx.io"

client = mqtt_client.Client(f'dz_{random.randint(10000, 99999)}')
client.on_message = on_message

try:
    client.connect(broker)
except Exception:
    print('Failed to connect. Check network')
    exit()

client.loop_start()

print('Subscribing')
client.subscribe("dz/hava/image/stream")
time.sleep(600)
client.disconnect()
client.loop_stop()
print('Stop communication')