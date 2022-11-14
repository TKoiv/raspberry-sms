import random
import sqlite_user
from matrixKeypad_RPi_GPIO import keypad
from time import sleep
import arduinoDev


class PinCode:
    kp = keypad()
    
    def digitreturn():
        # Loop while waiting for a keypress
        r = None
        while r == None:
            r = PinCode.kp.getKey()
        return r 


    #Call this function read your PIN-code and compare it whit password. 
    def pin():
        lockCounter = 0
        pinCode = []
        pin = 0
        digitCount = 0
        pin = [0,0,0,0]
        finalPin = "000"
        password = 0000

        while True:
            digit = PinCode.digitreturn()
            print(digit)
            pin[digitCount] = digit
            digitCount = digitCount + 1
            sleep(0.25)
            if digitCount == 4:
                finalPin = (str(pin[0]) + str(pin[1]) + str(pin[2]) + str(pin[3]))
                print(finalPin)          
                #print("Pinkoodin pituus = ",finalPin)
                if finalPin == "****":
                    arduinoDev.communicationLock()
                    digitCount = 0
                else:
                    finalPinInt = int(finalPin)
                    password = sqlite_user.getUser(finalPinInt)
                    #print("Password is: ",password)
                    #print("Pincode is: ",finalPin)
                    if password == 0:
                        print("Wrong pin-code try again!")
                        lockCounter += 1
                        digitCount = 0
                        #print(lockCounter)
                    elif finalPinInt == password:
                        print("Open lock!")
                        arduinoDev.communication()
                        lockCounter = 0
                        digitCount = 0
                
                    
            if lockCounter == 3:
                print("Kirjautuminen estetty")
                return lockCounter
            
#PinCode.pin()