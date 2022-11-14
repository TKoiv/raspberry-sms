#!/usr/bin/python

import RPi.GPIO as GPIO
import serial
import time
import sqlite_user
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, GPIO.LOW)


ser = serial.Serial("/dev/ttyS0",115200)
ser.flushInput()

global phone_number
phone_number = '+358407308301' 
text_message = ''
power_key = 6
rec_buff = ''

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
	return True

def power_down(power_key):
	print('SIM7600X is loging off:')
	GPIO.output(power_key,GPIO.HIGH)
	time.sleep(3)
	GPIO.output(power_key,GPIO.LOW)
	time.sleep(18)
	print('Good bye')

smsMessage = 0



class SMS:
	def definionData(data):
		SMS.phone_number = data
		#print(data)

	def send_at(command,back,timeout):
		rec_buff = ''
		ser.write((command+'\r\n').encode())
		time.sleep(timeout)
		global smsMessage
		
		
		if ser.inWaiting():
			time.sleep(0.01 )
			rec_buff = ser.read(ser.inWaiting())
		if rec_buff != '':
			#print(rec_buff.decode())
			if 'New pin' in rec_buff.decode(): sqlite_user.addUser(),time.sleep(3)
			#if back not in rec_buff.decode():print(command + ' back:\t' + rec_buff.decode())
			return 0
		else:
			global TEXTDATA
			TEXTDATA = str(rec_buff)
			#print(TEXTDATA)
			return 1
		
		
	def ReceiveShortMessage():
		rec_buff = ''
		#print('Setting SMS mode...')
		SMS.send_at('AT+CMGF=1','OK',1)
		SMS.send_at('AT+CMGL="REC UNREAD"', 'OK', 1)
		answer = SMS.send_at('AT+CMGL="REC UNREAD"', '+CMTI', 1)

	def deleteMessages():
		SMS.send_at('AT+CMGD=[,4]','OK', 1)



#power_on(power_key)
#while True:
#	SMS.ReceiveShortMessage()
#SMS.deleteMessages()
