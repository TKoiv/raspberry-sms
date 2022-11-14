
from locale import format_string
import sqlite3
from PasswordMaker import PasswordMaker
from datetime import datetime
from datetime import datetime, timedelta
import smsSend

conn = sqlite3.connect('Lock.db')

c = conn.cursor()
global phone_number
phone_number = '+358407308301'



#c.execute(""" CREATE TABLE user (
#            pinCode INTEGER,
#            perioid INTEGER,


#            )""") 

            


def addUser():
    now = datetime.now()
    currentDate = now.strftime("%-d%-m%Y")
    #print(currentDate)
    conn = sqlite3.connect('Lock.db')
    c = conn.cursor()
    pinCode = 0
    pinCode = PasswordMaker.passwordMaker()
    #print(pinCode)
    c.execute("INSERT INTO user VALUES (NULL,{},{})".format(pinCode, currentDate))
    pinCode = str(pinCode)
    txt_message = str("New PIN-code is: " + pinCode)
    #print(phone_number)
    #print(txt_message)
    smsSend.SendShortMessage(phone_number,txt_message)
    conn.commit()
    conn.close()
    return pinCode

def getUser(pinCode):
    conn = sqlite3.connect('Lock.db')
    c = conn.cursor()
    pin = 0
    try:
        c.execute("SELECT pinCode FROM user where pinCode={}".format(pinCode))
        #print(c.fetchall())
        for pin in c.fetchall():
            pin = pin
            #print("Pin koodi on:",pin)
            for pin in pin:
                pin = pin
                #print("Pin koodi2 on:",pin)
    except:
        pin = 0
    conn.close()
    return pin
    
    

def removeUser():
    yesterday = datetime.now() - timedelta(1)
    yesterday = yesterday.strftime("%-d%-m%Y")
    print(yesterday)
    conn = sqlite3.connect('Lock.db')
    c = conn.cursor()
    c.execute("DELETE from user WHERE date={}".format(yesterday))
    print("\nUser removed")
    conn.commit()
    conn.close()



#removeUser()

#addUser()
#c.execute("INSERT INTO user VALUES (NULL,{}, 1)".format(2188))
#pinkoodi69 = getUser(6425)

#print(pinkoodi69)
#c.execute("SELECT * FROM user where pinCode={} ".format(6425))
#print(c.fetchall())
#c.execute("SELECT * FROM user")

#c.fetchall()
#c.fetchmany(5)

#c.execute("SELECT pinCode FROM user where pinCode={}".format(6425))
#print(c.fetchall())

conn.commit()

conn.close()
