# Coursera
# An Introduction to Interactive Programming in Python
import random
def name_to_number(name):
	if name == 'rock':
		return 0
	elif name == 'Spock':
		return 1
	elif name == 'paper':
		return 2
	elif name == 'lizard':
		return 3
	else:
		return 4


def number_to_name(number):
	if number == 0:
		return 'rock'
	elif number == 1:
		return 'Spock'
	elif number == 2:
		return 'paper'
	elif number == 3:
		return 'lizard'
	else:
		return scissors
	
def rpsls(name):
	my_number = name_to_number(name)
	comp_number = random.randrange(0,4)
	print "Player choose "+name
	print "Computer choose "+number_to_name(comp_number)
	if(my_number - comp_number == 1 or my_number - comp_number == 4):
		print "Player wins!"
	elif(comp_number - my_number == 1 or comp_number - my_number == 4):
		print "Computer wins!"
	elif(my_number - comp_number == 2):
		print "Player wins!"
	elif comp_number - my_number == 2:
		print "Computer wins!"
	elif my_number - comp_number == 3:
		print "Computer wins!"
	elif comp_number - my_number == 3:
		print "Player wins!"
	else:
		print "play again!"
	
name1 = 'rock'
rpsls(name1)