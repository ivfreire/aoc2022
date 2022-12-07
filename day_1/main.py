#!/bin/python3

with open('input', 'r') as file:
	data = file.readlines()

	cals = [ 0, 0 ]

	for line in data:
		if line == '\n':
			if cals[0] > cals[1]: cals[1] = cals[0]
			cals[0] = 0
		else:
			cals[0] += int(line[0:-1])
	
	print(f'The eld carrying the most callories is carrying a total of {cals[1]} callories.')