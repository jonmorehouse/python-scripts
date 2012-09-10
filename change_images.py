#!/usr/bin/python

import sys, os, commands
source_directory = "~/Desktop/parallax_background/"
destination_directory = "~/Desktop/parallax_images/"
width = 800

for i in range(1, 83):

	source = "%s%s.png" % ( source_directory, i)

	i += 10

	destination = "%s%s.png" % (destination_directory, i)

	command = "sips --resampleWidth %s %s --out %s" % (width, source, destination)

	print commands.getoutput(command)

