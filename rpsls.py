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
	
	
name1 = 'rock'
number1 = 3
print str(name_to_number(name1))
print number_to_name(number1)