import paho.mqtt.client as mqtt_client
from statistics import mean
import serial

min = 100
max = 0

broker="broker.emqx.io"
client = mqtt_client.Client()
client.connect(broker)
ser = serial.Serial("COM6", timeout=1)

while True:
    if ser.in_waiting > 0:
        data = ser.read(1)
        if min > data[0]:
            min = data[0]
        client.publish("dz/hava/image/photo/min", min)
        if max < data[0]:
            max = data[0]
        client.publish("dz/hava/image/photo/max", max)
        print("Value: " + str(data[0]) + "\nmin: " + str(min) + ", max: " + str(max))
client.disconnect()
