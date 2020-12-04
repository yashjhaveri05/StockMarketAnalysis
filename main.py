from stockreturn import *
from close import *

def start():
    print()
    print("1.Alphabet Close Price Graph")
    print("2.Microsoft Close Price Graph")
    print("3.Facebook Close Price Graph")
    print("4.IBM Close Price Graph")
    print("5.Amazon Close Price Graph")
    print("6.ALL 5 Close Price Graph")
    print("7.Stock Return Price Graph")
    print()
    val = int(input("Enter Choice: "))
    if(val == 1):
        google_func()
        start()
    elif(val == 2):
        microsoft_func()  
        start()
    elif(val == 3):
        facebook_func()
        start()
    elif(val == 4):
        ibm_func()
        start()
    elif(val == 5):
        amazon_func()
        start()
    elif(val == 6):
        combination()
        start()
    elif(val == 7):
        plot()
        start()
    else:
        print("Incorrect")
        exit()

start()