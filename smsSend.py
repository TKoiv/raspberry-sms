#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO

import serial
import time

ser = serial.Serial('/dev/ttyS0',115200)
ser.flushInput()

power_key = 6
rec_buff = ''
time_count = 0


def power_on(power_key):
	print('SIM7600X is starting:')
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(power_key,GPIO.OUT)
	time.sleep(0.1)
	GPIO.output(power_key,GPIO.HIGH)
	time.sleep(2)
	GPIO.output(power_key,GPIO.LOW)
	time.sleep(20)
	ser.flushInput()
	print('SIM7600X is ready')
	
def SendShortMessage(phone_number,text_message):
    ser.flushInput()
    print("\nSetting SMS mode...")
    send_at2("AT+CMGF=1","OK",1)
    print("\nSending Short Message\n")
    answer = send_at2("AT+CMGS=\""+phone_number+"\"",">",2)
	#power_down(power_key)
    if 1 == answer:
        ser.write(text_message.encode())
        ser.write(b'\x1A')
    else:
        print('error%d'%answer)
	#power_down(power_key)

def send_at2(command,back,timeout):
	rec_buff = ''
	ser.write((command+'\r\n').encode())
	time.sleep(timeout)
	if ser.inWaiting():
		time.sleep(0.01 )
		rec_buff = ser.read(ser.inWaiting())
	if back not in rec_buff.decode():
		#print(command + ' ERROR')
		#print(command + ' back:\t' + rec_buff.decode())
		return 0
	else:
		print(rec_buff.decode())
		return 1
