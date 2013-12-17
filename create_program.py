#!/usr/bin/python

"""
	1.) This program will get the current path
	2.) This program will create a file (given the name)
	3.) This program will create the correct program information in the top line -- unless given a third parameter

"""

import os, sys, subprocess

"""
	FUNCTIONS
""" 

def get_program_type(file_name):

	extension = file_name.split(".")

	program_map = {}
	program_map['py'] = "python"
	program_map['sh'] = "bash"
	program_map['rb'] = "ruby"
	program_map['py3'] = "python3"
	program_map['php'] = "php"
	program_map['js'] = "node"

	if not extension[-1] or not extension[-1] in program_map:
		return False

	else:
		return program_map[extension[-1]]


def create_program(file_name, program_type):

	location = subprocess.check_output(["which", program_type]).strip()

	contents = "#!" + location + "\n"

	program_file = open(file_name, 'w').write(contents)
	
	subprocess.call(["chmod", "+x", file_name])


"""
	PROGRAM RUN
"""

if not len(sys.argv) > 1:

	print "Please input file name"
	sys.exit()

else:
	file_name = sys.argv[1]
	
	if not len(sys.argv) > 2: 

		program_type = get_program_type(file_name)

		if not program_type:
			print "Invalid file extension. Run like -file_name -program"
			sys.exit()

	else: program_type = sys.argv[2]

	create_program(file_name, program_type)
