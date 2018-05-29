from sense_hat import SenseHat
from random import randint
from time import sleep
sense=SenseHat()
num1=randint(0,255)
num2=randint(0,255)
num3=randint(0,255)
sense.clear(num1,num2,num3)
sleep(1)
sense.clear()