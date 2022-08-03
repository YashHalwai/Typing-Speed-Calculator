# Typing Speed Calculator

from time import *
import random as r

print(time())

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error                

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput) / time_R

    return round(speed) 
if __name__ == '__main__':

 while True:
    ck = input(" Ready to test : yes / no : ")
    if ck == "yes": 
       test = ["Google LLC is an American multinational technology company that focuses on search engine technology, online advertising, cloud computing, computer software, quantum computing, e-commerce, artificial intelligence, and consumer electronics","Microsoft Corporation is an American multinational technology corporation which produces computer software, consumer electronics, personal computers, and related services headquartered at the Microsoft Redmond campus located in Redmond, Washington, United States","Uber Technologies, Inc. is an American mobility as a service provider, allowing users to book a car and driver to transport them in a way similar to a taxi. It is based in San Francisco with operations in pproximately 72 countries and 10,500 cities in 2021."] 
       test1 = r.choice(test)
       print("   ******* Typing Speed Calculator *******   ")

       print(test1)

       print()
       print()
       time_1 = time()
       testinput = input(" Enter : ") 
       time_2 = time()

       print("Speed : ", speed_time(time_1,time_2,testinput), " w/sec")
       print("Error : ", mistake(test1,testinput))

    elif ck == "no":
        print("Thank You :)")
        break


    else:
        print("Wrong Input")       
