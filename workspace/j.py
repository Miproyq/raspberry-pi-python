from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
while True:
    acceleration=sense.get_accelerometer_raw()
    x=acceleration['x']
    y=acceleration['y']
    z=acceleration['z']
    x=round(x,0)
    y=round(y,0)
    z=round(z,0)
    print("x={0},y={1},z={2}".format(x,y,z))
    sleep(.1)
    sense.show_letter("j")
    if x==-1: sense.set_rotation(90)
    if y==1: sense.set_rotation(0)
    if y==-1:sense.set_rotation(180)
    if x==1:sense.set_rotation(270)
    
