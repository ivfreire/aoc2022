#!/bin/python3

with open('input', 'r') as file:
	data = file.readlines()

	elves = [ [ 0 , 0 ], [ 0, 0 ], [ 0, 0 ] ]
	elf, cals = 0, 0

	for line in data:
		if line == '\n':

			for i in range(len(elves)):
				if cals > elves[i][1]:
					elves[i] = [ elf, cals ]
					break

			cals = 0
			elf += 1
		else:
			cals += int(line[0:-1])
		
	tot = 0
	for elf in elves: tot += elf[1]
	print(f'The total number of calories carryed by the top three elves is {tot} calories.')