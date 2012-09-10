#!/usr/bin/python
from classes import files, cleaner, github

import json, os

# EACH PROJECT EXTENDS GITHUB_UPDATE WHICH IS RESPONSIBLE FOR RUNNING THESE COMMANDS
# ALL PROJECTS ARE WITHOUT THE TRAILING SLASH

configuration_file = "/Users/DefaultPassword/Documents/general_development/helper_programs/python/github_update/configuration.json"

with open(configuration_file) as configuration:
    configuration = json.load(configuration)


class Github_update(object):

	cleaner = cleaner.Cleaner(configuration['credentials'], configuration['sed_banned_file_types']) #this is the parent that holds the credentials to be replaced for all the different projects -- universal -- this is used throughout the class's different instantiated files
	deleted_files = [] # this will last throughout all of the different objects 
 
	def __init__(self, configuration):

		self.configuration = configuration #this is the configuration for this entire project
		self.file_list = [] #these are the destination files that need to be "cleansed"
		self.github = False #we need to set this variable true if this particular project requires github update


	def synchronize(self): #this is responsible for synchronizing and will update 

		# source files to be sent to the synchronization list
		source = files.File_list(self.configuration['source'], self.configuration['banned_files'], self.configuration['banned_directories'])
		source_list = source.get_file_list().file_list

		# destination list -- to be sent to the synchronization
		destination = files.File_list(self.configuration['destination'], self.configuration['banned_files'], self.configuration['banned_directories'])
		destination_list = destination.get_file_list().file_list

		# send the directories to the synchronization list
		directories = dict()
		directories['source'] = self.configuration['source']
		directories['destination'] = self.configuration['destination']

		# SYNCHRONIZE CLEANS THE FILES
		synchronize = files.File_synchronization(source_list, destination_list, directories, self.configuration['project_name'])
		synchronize.synchronize()

		if len(synchronize.synchronization_list) > 0:
			self.github = True #this project needs to be updated on github

		for item in synchronize.synchronization_list:
			self.file_list.append(item['destination']) #add the destinations because we only want to clean those files

		self.deleted_files.extend(synchronize.deleted_files) #extend the class's parent with the files that were deleted -- can call a method on this later -- it's extended

		return self

	def github_update(self): 


		if self.github and len(self.file_list) > 0: #need to make sure the github update is even necessary -- then prompt the user again!

			message  = "Would you like to update github for %s? (y/n):" % self.configuration['project_name']

			answer = raw_input(message)

			if answer.lower() == "y":
				github.Github(self.configuration['github']).update() #send the github class the the github credentials for this project

		else:
			print "No github update necessary %s" % self.configuration['project_name']

		return self

	def clean(self): #will run the clean utilities on all of the files given -- the files given will be a class that is instantiated before hand with the credentials -- we can also send it custom words for that project only

		destination_list = files.File_list(self.configuration['destination'], [], configuration['sed_banned_directories']).get_file_list() #dont need to send the banned files/directories because they have already been used -- this is a clean directory == we just need all the files for the cleaning function
		_cleaner = cleaner.File_cleaner(self.configuration['credentials']) #pass the file_cleaner (which is a child of the parent, the credentials for this project)

		for item in destination_list.file_list:

			_cleaner.clean_file(item['path']) #this will just be a straight path at this point and then just call the sed cleaner!

		return self


for project in configuration['projects']:

	backup = Github_update(project).synchronize()

	if project['clean_files']:
		backup.clean()

	if project['github_backup']:
		backup.github_update()




