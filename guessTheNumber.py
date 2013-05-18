# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
num_range = 100

# define event handlers for control panel


def range100():
    global num_range
    num_range = random.randrange(0,100)
    return num_range
    
def range1000():
    global  num_range
    num_range = random.randrange(0,1000)
    return num_range
    
    # button that changes range to range [0,1000) and restarts
    
def get_input(guess):
    guess = int(guess)
    if guess == num_range:
        print "correct"
    elif guess > num_range:
        print "goal is "+str(num_range)+", current is "+str(guess)+",higher!"
        guess = guess - 1
        get_input(guess)
    else:
        print "goal is "+str(num_range)+", current is "+str(guess)+", lower!"
        guess = guess + 1
        get_input(guess)

    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)
f.add_input("Enter a guess", get_input, 200)


# start frame


# always remember to check your completed program against the grading rubric
