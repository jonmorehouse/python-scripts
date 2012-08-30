#!/usr/bin/python

# 1.) Load configuration files / folders
# 2.) Sequential deployment
# 3.) Compile/compress javascript/css/static 
# 4.) Deploy static to different media/static
# 5.) Update python files
# 6.) Dump local db and update remotely
# 7.) (backup both of these)

import os, commands, sys, string, subprocess

from utilities.bash import Utilities
from configuration import Rip_it_up_world

class Deploy(object):
	
	def __init__(self):
		print "hello from the deploy section"
		selection()
		

	def selection():#responsible for validating the selection
		
		if (not len(sys.argv) > 1):
			return sys.exit("Not a valid selection")

		elif (sys.argv[1].lower() == "rip_it_up_world"):
			self.project = "rip_it_up_world"
			self.configuration = Rip_it_up_world()
			return self
			
		else:
			return sys.exit("Not a valid selection")
	
	
	def amazon(): # will be responsible for checking the amazon and then doing what is necessary for that
		if (configuration.media_type == "amazon"):
			print "media type is amazon!"
		
		if (configuration.static_type == "amazon"):#will also call a class to compile if necessary -- but that is in the configuration because not used everywhere
			print "static type is amazon"
	
			
	def site(): #will be responsible for checking the site url and updating dotcloud or ssh
		
		if (server == "dotcloud"):#will cd to the proper directory and then upload
			
			print "dotcloud site"

		elif (server == "ssh"): #will just do a plain vanilla update -- relies on key though
			# will send the directory
			
	

		
		
		 




# 	
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
