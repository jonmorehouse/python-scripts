#!/usr/bin/python
import sys, os

message = "json_compressor -o output input.json"

def _read(argv):

	input_file = argv[-1]

	try:

		data = open(input_file, 'r').read()
		data = data.replace("\n", "")
		return data

	except IOError:

		print "Bad file"
		print message
		exit()

	#end method

def _write(filename, data):

	try:

		with open(filename, 'w') as writer:

			writer.write(data)

	except IOError:

		print "Could not write data. Please try again"
		print message



def main(argv = sys.argv):

	if len(argv) <= 1: 

		print message
		exit()

	data = _read(argv)

	if len(data) == 0:
		print "Empty file. Please try again."
		print message
		exit()

	if len(argv) == 4 and argv[1] == "-o":

		_write(argv[2], data)

	else:

		print data

main(sys.argv)
