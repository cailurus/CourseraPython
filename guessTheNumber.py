# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random

# initialize global variables used in your code


# define event handlers for control panel
    
#def range100():
    # button that changes range to range [0,100) and restarts

#def range1000():
    # button that changes range to range [0,1000) and restarts
    
def get_input(guess):
	goal = random.randrange(0,100)
	if(guess == goal):
		print "My guess is "+str(guess)+", and the goal is "+str(goal)+", so it's correct!"
	elif(guess > goal):
		print "My guess is "+str(guess)+", and the goal is "+str(goal)+", so it's higher!"
		get_input(guess)
	else:
		print "My guess is "+str(guess)+", and the goal is "+str(goal)+", so it's lower!"
		get_input(guess)
	
get_input(40)
    
# create frame


# register event handlers for control elements


# start frame


# always remember to check your completed program against the grading rubric
