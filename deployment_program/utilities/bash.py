import os, commands


# THIS IS A UTILITIES CLASS TO HELP WITH FUNCTIONS THAT ARE COMMON AROUND THE BASH SHELL

# THIS FUNCTION IS USEFUL FOR COMBINING FILES DYNAMICALLY
def combine(output_file, input_files):
	# ASSUMES THE INPUT FILES ARE FULL PATHS
	# WILL CHECK FOR THE EXISTISTENCE OF EACH ONE
	
	print "testing123"
	command = "cat "
	for input_file in input_files:
		
		command += input_file + " "
	
	command += "> %s" % output_file 


	
	commands.getstatusoutput(command)	


# USES THE INSTALLED YUI EDITOR TO PERFORM THIS FUNCTION -- works for either css or javascript files
def compress(input_file):
	
	tmp_file = "/tmp/deployment_temp"
	compress = "yuicompressor %s > %s" % (input_file, tmp_file)
	move = "mv %s %s" % (tmp_file, input_file)
		
	commands.getstatusoutput(compress)
	commands.getstatusoutput(move)

		
# make a directory for the temporary files, then compile all files into the directory, and then combine all the files
def less_compile(input_file, output_file):

	compile = "lessc %s %s" % (input_file, output_file)

	commands.getstatusoutput(compile)


def mkdir(folder):

	
	command = "mkdir %s" % folder
	
	commands.getstatusoutput(command)


def rmdir(folder):

	command = "rm -rf %s" % folder
	commands.getstatusoutput(command)


def folder_combine(folder, output_file):

	# this function is going to combine all of the files in the folder ( which is the temp folder )
	# into the output_file

	command = "cat %s* > %s" % (folder, output_file)

	commands.getstatusoutput(command)


def mysql_dump(credentials, output_file): #responsible for dumping database locally
	
	location = commands.getoutput("which mysqldump")

	if not credentials.has_key("database"):
		database = "--all-databases"
	else:
		database = credentials["database"]

	command = "%s -u%s -p%s %s > %s" % (location, credentials["username"], credentials["password"], database, output_file)

	commands.getstatusoutput(command)
	







	







