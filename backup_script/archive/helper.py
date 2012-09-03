import os # import the system -- allows you to run any command you want with bash
import commands # commands.getoutput() allows you to get the command output
import sys # allow python to grab the argument
import string
import configuration
import helper
import backup

def file_list(directory):
	bash_command = "cd %i && find . *" % directory
	string_list = commands.getoutput(bash_command)
	files = string.split(test, '\n')
	
	return files