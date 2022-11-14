import serial
import time

def communication():
    
    ser = serial.Serial('/dev/ttyUSB2', 9600, timeout=1)
    ser.reset_input_buffer()
    i = 0
    while i < 3:
        ser.write("1".encode('utf-8'))
        time.sleep(1)
        #ser.write("0".encode('utf-8'))
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)
        i += 1

def communicationLock():
    
    ser = serial.Serial('/dev/ttyUSB2', 9600, timeout=1)
    ser.reset_input_buffer()
    i = 0
    while i < 3:
        ser.write("0".encode('utf-8'))
        time.sleep(1)
        #ser.write("0".encode('utf-8'))
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)
        i += 1

def communicationOpen():
    
    ser = serial.Serial('/dev/ttyUSB2', 9600, timeout=1)
    ser.reset_input_buffer()
    i = 0
    while i < 3:
        ser.write("3".encode('utf-8'))
        time.sleep(1)
        #ser.write("0".encode('utf-8'))
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)
        i += 1




#communication()