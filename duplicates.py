#!/usr/bin/python

inputs = [1, 4, 4,4,5,6,6,7, 111, 21]

"""
	Slower solution which requires a bit more memory overhead but very trivial to work with
"""
def uniques(inputs):

	# this is really slow because of the look up times on the element
	found = []

	for i in inputs:	

		if i in found: continue

		found.append(i)

	return found	

def inplace_uniques(inputs):

	found = {}
	position = 0

	for i in inputs:

		# if our i is not in the hash already then we need to go ahead and add it
		if i not in found:

			found[i] = True
			inputs[position] = i
			position += 1		

	# delete all of the elements that have not been found
	del inputs[position:]			


inplace_uniques(inputs)
uniques(inputs)

	



