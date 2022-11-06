import paho.mqtt.client as mqtt_client
from statistics import mean
import serial

interval = 100
do_calibrate = True
steps = 0

broker="broker.emqx.io"
client = mqtt_client.Client()
client.connect(broker)
ser = serial.Serial("COM6", timeout=1)

while True:
    if ser.in_waiting > 0:
        if ser.in_waiting >= 2 or interval <= 0:
            do_calibrate = False
            interval += 1
        print("In waiting: " + str(ser.in_waiting))
        data = ser.read(1)
        print("Value: " + str(data[0]))
        client.publish("dz/hava/image/stream", data[0])
        ser.write(bytearray([int(ord("I")), int(interval)]))
        print("Interval: " + str(interval))
        if do_calibrate:
            if steps % 10 == 0:
                interval -= 1
        steps += 1
        print("==============\n")
client.disconnect()