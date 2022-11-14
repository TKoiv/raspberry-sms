import random

class PasswordMaker:

    #Call this function you get 4 digits random password whit range 0-9. Function return list. 
    def passwordMaker():
        randomPassword = []
        randomPassword.append(random.randint(1000,9999))
        if randomPassword == ([1234] or [9876] or [1111] or [2222] or [3333] or [4444] or [5555] or [6666] or [7777] or [8888] or [9999] or [4321] or [0000]):
            print("Call new password")
            PasswordMaker.passwordMaker()
        else:
            #print(randomPassword)
            i = 0
            for i in randomPassword:
                return i
