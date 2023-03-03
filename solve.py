# Math assignment puzzle solver 
# Author: Saku (saku.lol)

from itertools import permutations
import random
import os


# Values that are unused in the grid
inputList = [[1, 2, 3, 4, 5, 8, 14, 15]] 

# Values that are used to validate the grid
inputValidation = [[34, 25, 31, 46]] 

# Values which are already in the grid and the sum of the row
inputGrid = [[[[0, 10, 0, 12], 29], [[16, 0, 6, 0], 35], [[0, 0, 7, 0], 25], [[13, 9, 0, 11], 47]]]



def findAnswer(vG, tN):
	# Process inputs by permutating all possible outcomes
	pL = [list(i) for i in permutations(inputList[tN])]
	fL = []
	i = 0
	
	
	# Filter values by looping thru processed list
	while len(pL) != 0:
		if (sum(pL[0][:vG[0][0].count(0)]) + sum(vG[0][0])) == vG[0][1]:
			fL.append(pL[0])
		pL.pop(0)

	i += vG[0][0].count(0)
	lF = []

	for vR in vG[1:]:
		while len(fL) > 1 and not i >= len(inputList[tN]):
			if sum(fL[0][i:i+vR[0].count(0)]) + sum(vR[0]) == vR[1]:
				lF.append(fL[0])
			fL.pop(0)
		i += vR[0].count(0)


	# Validate filters and find correct answer
	for v in lF:
		fV = []
		for i, r in enumerate(vG):
			tR = []
			for n in r[0]:
				if n == 0: tR.append(v.pop(0))
				else: tR.append(n)
			fV.append(tR)

		if [sum(row[i] for row in fV) for i in range(len(fV[0]))] == inputValidation[tN]: return fV
	
	return False




if __name__ == "__main__":
	os.system('cls' if os.name == 'nt' else 'clear')
	print("Etsitään vastausta...", end="\n\n")
	ans = findAnswer(inputGrid[0], 0)

	if ans != []:
		print("Vastaus:", end="")
		for row in ans:
			print("")
			print(*row, sep=' ', end=" ")
		print("\n\n")
	else:
		print("Vastausta ei löytynyt :(")