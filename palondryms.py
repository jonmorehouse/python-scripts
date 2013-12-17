#!/usr/bin/python
"""
	Determine whether or not an element is a palondrym etc
"""
def checkPalondrym(inputString):

	length = len(inputString)

	for i in range(length/2):

		# remember to start the string at length-1
		if inputString[i] != inputString[length-1-i]:

			return False

	return True		





	
print checkPalondrym("JonMorehouse")
print checkPalondrym("racecar")





