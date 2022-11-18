import sqlite_user
import pinCode
from datetime import datetime
import smsCom
import time
from multiprocessing import Process
import phonenumber as pnumber
import smsSend

global phone_number
phone_number = pnumber.phone_number

def loop_SMS():
    while True:
        smsCom.SMS.ReceiveShortMessage()

def loop_USER():
    i = 0
    while True:
        now = datetime.now()
        time = now.strftime("%H:%M")
        if (time > "12:00" and time < "12:30"):
            while i < 2:
                print("\nUsers deleted")
                sqlite_user.removeUser()
                smsCom.SMS.deleteMessages()
                i += 1
        if (time == "13:00"):
            i = 0
            continue

#def loop_PIN():
#    while True:
#        pinCode.PinCode.pin()

if __name__ == "__main__":
    text_message = ''
    smsModule = smsCom.power_on(6)
    if smsModule == True:
        Process(target=loop_SMS).start()
        Process(target=loop_USER).start()
        #Process(target=loop_PIN).start()
        while True:
            lockCounter = pinCode.PinCode.pin()
            if lockCounter == 3:
                print("Too many gues login denied!")
                txt_message = str("Too many gues login denied!")
                smsSend.SendShortMessage(phone_number,txt_message)
                continue


            
    #print(phone_number)
    #print(txt_message)
    