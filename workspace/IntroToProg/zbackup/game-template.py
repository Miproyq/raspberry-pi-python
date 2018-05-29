# IMPORT the required libraries (sense_hat, time, random) 
from sense_hat import SenseHat
from time import sleep
from random import choice

# CREATE a sense object
sense = SenseHat()

# Set up the colours (white, green, red, empty)

w = ???
g = ???
r = ???
e = ???

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

arrow_red = [
e,e,e,r,r,e,e,e,
e,e,r,r,r,r,e,e,
e,r,e,r,r,e,r,e,
r,e,e,r,r,e,e,r,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e
]

arrow_green = [
e,e,e,g,g,e,e,e,
e,e,g,g,g,g,e,e,
e,g,e,g,g,e,g,e,
g,e,e,g,g,e,e,g,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e
]

# Set a variable pause to 3 (the initial time between turns)  
# Set variables score and angle to 0  
# Create a variable called play set to True (this will be used to stop the game later)  
pause = ???
score = ???
angle = ???
play = ???

sense.show_message("???", scroll_speed=0.05, text_colour=[100,100,100])

# WHILE play == True 
while play:
  
    # CHOOSE a new random angle. How do we avoid choosing the same angle as the last one? 
	????????     #one or more lines

    sense.set_rotation(angle)
    
    # DISPLAY the white arrow
	???
    
    # SLEEP for current pause length  
    ???
    
    # get raw acceleromter readings
    ???
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
	
	# round x and y to Zero Decimal Places


    print(angle)
    print(x)
    print(y)

    # IF orientation matches the arrow...
    if x == -1 and angle == 180:
        # ADD a point to the score and turn the arrow green  
        ???
        ???
    # code for rest of the if structure. use the keyword 'elif'.  Remember the indentation!
	elif ???
	
	?????????

	# the last else statetment. All siutation which doesn't falls under the conditions above will be handled here. For this case, that means user got the answer wrong.
    else:
      # SET play to `False` and DISPLAY the red arrow
      ???
      ???

    # Shorten the pause duration slightly.  Hint: multiply pause variable by a number smaller than 1.  
    ???
    
    # Pause before the next arrow 
    sleep(0.5)

# When loop is exited, display a message with the score  
msg = "Your score was %s" % score
sense.show_message(msg, scroll_speed=0.05, text_colour=[100, 100, 100])