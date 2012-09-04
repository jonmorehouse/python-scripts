import configuration
import options

from configuration import *
from options import *

# We know that the command exists, now just need to perform the backup!
# strings, ints some other things are passed by value not refrenec

def main(input):
	
	source = backups[i].source
	destination = backups[i].destination
	source_files = []
	destination_files = []
	file_list(source, source_files)
	destination_list(destination, destination_files)
	
	backup_needed(source_list, destination_list)
	
	
	return
	
def file_list(directory, list):
	
	return
	
def backup_needed(source_list, destination_list):
	
	return
	
