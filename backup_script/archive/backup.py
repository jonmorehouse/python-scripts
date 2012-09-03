import os, commands, sys, string, configuration, helper, backup

def main(backup):#main program function
	
	if backup in configuration.backups:#validate the function one more time
		i = configuration.backups.index(backup)#find the index of the backup command currently being used
		source_list = helper.file_list(configuration.source[i])
		
		
	
	return

