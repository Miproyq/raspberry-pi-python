from sense_hat import SenseHat
from random import randint
from time import sleep
sense=SenseHat()
for i in range(1000):
    for b in range(8):
        for a in range(8):
            num1=randint(0,255)
            num2=randint(0,255)
            num3=randint(0,255)
            r=(num1,num2,num3)
            sense.set_pixel(a,b,r)
            sleep(0)
sense.clear()
    

