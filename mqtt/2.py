import paho.mqtt.client as mqtt_client
from statistics import mean
import serial

broker="broker.emqx.io"
client = mqtt_client.Client()
client.connect(broker)
ser = serial.Serial("COM6", timeout=1)
initial = True
while True:
    if ser.in_waiting > 0:
        data = ser.read(1)
        if initial:
            values = [data[0] for i in range(100)]
            initial = False
        values.pop(0)
        values.append(data[0])
        client.publish("dz/hava/image/averge", mean(values))
client.disconnect()
