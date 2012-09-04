#!/usr/bin/python

from classes.files import File_list, File_synchronization

# THIS TEST IS FOR TESTING THAT THE FILE LISTS GENERATE CORRECT LISTS

directory = "~/Desktop/test_source"
banned_directories = []
# banned_directories = ["test_source", "test_destination"]
banned_list = ["\*\.zip", "test_source/3.md"]


def file_list():
	
	c = File_list(directory, banned_list, banned_directories)
	c.get_file_list()
	c.clean_file_list()


	for i in c.file_list:
		print "path = " + i["path"]
		print "name = " + i["name"]
		print "\n"



def file_sync(): #this function is responsible for testing the files between the two folders
	
	source = "~/Desktop/test_source/"
	destination = "~/Desktop/test_destination/"


	banned_directories = []
	banned_list = []

	source = File_list(source, banned_list, banned_directories).get_file_list()
	destination = File_list(destination, banned_list, banned_directories).get_file_list()


	c = File_synchronization(source.file_list, destination.file_list, "TestSource")

	c.synchronize()

# file_list() #working right now
file_sync() 
