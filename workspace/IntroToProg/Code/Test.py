from sense_hat import SenseHat
from time import sleep
from random import choice
sense = SenseHat()
sense.clear()
while True:
    acceleration=sense.get_accelerometer_raw()
    x=acceleration['x']
    y=acceleration['y']
    z=acceleration['z']
    x=round(x,0)
    y=round(y,0)
    z=round(z,0)
    print("x={0},y={1},z={2}".format(x,y,z))
    
    