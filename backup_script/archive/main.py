import os # import the system -- allows you to run any command you want with bash
import commands # commands.getoutput() allows you to get the command output
import sys # allow python to grab the argument
import string
import configuration
import helper
import backup

# from configuration import * #import all variables

bash_command = "cd ~/Documents/work && find . *"
# file_list = os.system(bash_command)

test = commands.getoutput(bash_command)
# files = string.split(test, '\n')
# print len(files)

user_input = sys.argv[1]
	
if user_input == "all":
	for i in configuration.backups:
		# backup.main(i)
		configuration.get_source(i)
