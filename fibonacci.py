#!/usr/bin/python

# create a fibonacci lambda
fibonacci = lambda previous, current: previous + current if previous + current > 0 else 1


# controller is useful for printing out valid information for the actual callback / lambda etc
def controller(previous, current, counter, callback):

	# grab the next element
	next = fibonacci(previous, current)

	# call the passed in callback etc for this element!
	callback(next)

	# now we want to recursively run this function!
	if counter > 0:

		return controller(current, next, counter-1, callback)


# create a basic print function
def printer(_input):

	# this is customizable!
	print "%d" % (_input)


# now initialize our fibonacci printer etc to do this properly!
controller(0,0,20,printer)