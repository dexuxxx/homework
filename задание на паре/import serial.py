#pip install pyserial

import serial
import time

def get_connection(port):
    ser = serial.Serial(port, timeout=1)
    return ser

def send(ser, message, mesg_len):
    ser.write(message)
    time.sleep(0.1)
    if mesg_len != 0:
        data = ser.read(mesg_len)
        result = data.decode()
        result = result.strip()
        print(result)

if name == 'main':
    ser = get_connection("COM4")
    while True:
        inp = input("Enter command: ")
        send(ser, inp.encode(), 0)