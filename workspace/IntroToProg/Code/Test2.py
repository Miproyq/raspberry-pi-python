from sense_hat import SenseHat
from time import sleep
from random import choice
sense = SenseHat()
w = (255,255,255)
g = (0,255,0)
r = (255,0,0)
e = (0,0,255)

# Create images for three different coloured arrows

arrow = [
e,e,e,w,w,e,e,e,
e,e,w,w,w,w,e,e,
e,w,e,w,w,e,w,e,
w,e,e,w,w,e,e,w,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e
]
angle=(90)
sense.set_rotation(angle)
sense.set_pixels(arrow)