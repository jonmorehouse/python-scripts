#!/usr/bin/python
# 1.) Load configuration files / folders
# 2.) Sequential deployment
# 3.) Compile/compress javascript/css/static 
# 4.) Deploy static to different media/static
# 5.) Update python files
# 6.) Dump local db and update remotely
# 7.) (backup both of these)

import os, commands, sys, string, subprocess

from utilities import *
from configuration import * #this will have all of our configuration objects



class Deploy(object):
	
	def __init__(self, project):
		
		
		self.project = project
		self.configuration = rip_it_up_world.Rip_it_up_world()
		
	
	


def selection():#responsible for validating the selection
	
	if (not len(sys.argv) > 1):
		return sys.exit("Not a valid selection")
		
	elif (sys.argv[1].lower() == "rip_it_up_world"):
		
		return Deploy(sys.argv[1].lower())
		
	else:
		return sys.exit("Not a valid selection")
		


deploy = selection() #will be responsible for calling the program -- will exit if not valid, will run the deploy object if valid







# print "asdf"

# ls = commands.getoutput('ls')
# string = "hello world this is jon"
# 
# subprocess.Popen('echo "%s"' %string, shell = True)
# 
# subprocess.Popen(['echo', string], shell = False)
# 
# path = "~/Documents"
# 
# subprocess.Popen(['cd'], shell = False)
# 
# Utilities().test()
