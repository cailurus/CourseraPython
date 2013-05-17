def name_to_number(name):
	if name == 'rock':
		return 0
	elif name == 'Spock':
		return 1
	elif name == 'paer':
		return 2
	elif name == 'lizard':
		return 3
	else:
		return 4

name1 = 'rock'
print str(name_to_number(name1))