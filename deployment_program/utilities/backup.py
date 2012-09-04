# class backup is responsible for taking directories, comparing the files, side by side and then returning a list of local files and their destinations
# 1.) Give to directory roots that are the same and generate a list of absolute files for each one (3 arrays, file_name from root, live absolute, local absolute)
# 2.) For each of the files, compare the date given, if local is greater than new, then put them in each of the new arrays (destination and source) pop them out of the list
# 3.) go through each list and copy the files correspondingly -- this method can be replaced in the children classes

import commands, os.path


class Backup(object):

	def __init__(self, source, destination):

		if self._exists(source) and self._exists(destination):

			self.source = source
			self.destination = destination

			return True
		
		else:
			return False #bad directory was given -- need to look into this should not happen

	# PROTECTED METHODS

	# THIS IS THE GENERAL BACKUP SCHEMA, TO BE USED IF BOTH DIRECTORIES ARE LOCALIZED
	def _backup(self):

		source = self.source
		destination = self.destination
		# GENERATE THE LIST'S FOR EACH ONE
		source_list = self._source_list(source) #return the source list to be used by the file_list and destination and copy functions
		self.file_list = self._file_list(source_list, source) #return the file list to be used by the destination to determine valid files

		destination_list = self._destination_list(destination) #return teh destination list to be used for comparison

		self._compare(source_list, destination_list) #this creates the global lists for the copy function to use

		self._synchronize() #finally run the synchronization of all the files 
		# generate a final compare_list (with self.source and self.destination coming out of it)


	def _exists(self, directory): #will return true / false depending upon whether the folders exist

		if os.path.exists(directory):
			return True

		else:
			return False


	def _source_list(self, directory): #generates a list of files in the source directory (absolute)

		return self.__directory_items(directory)


	def _destination_list(self, directory): #generates a list of files in the destination directory (absolute)

		destination_list = self.__directory_items(directory)


		file_list = self.file_list

		for item in destination_list:

			# get just the file name for each file in this list
			name = item.replace(directory, "")

			# now verify that each file is in the actual file list that we are using
			if name not in file_list:

				self._remove(item) #remove the item
				destination_list.remove(item) #remove item from destination list

		return destination_list

	# FILE LIST IS GIVEN PARAMETERS IN CASE THE SOURCE IS S3
	def _file_list(self, raw_file_list, source_directory): #generates a list of files in the local directory (relative)

		file_list = []
		
		# need to erase the self.source from each of the files -- also the directory names
		for item in raw_file_list:
			item = item.replace(source_directory, "")

			if item.find(".") != -1:
				file_list.append(item)
			
		
		return file_list


	# generates two global lists of items to be compared with
	def _compare(self, source_list, destination_list):

		# coming into this function, we already know that the destination file names are valid, because they were checked agains the file_list in the previous section
		self.source_list = []
		self.destination_list = []

		# loop through file list, check that it appears in both source_list and destination_list and then if it does, then compare!

		for item in self.file_list:

			source_item = self.source + item
			destination_item = self.destination + item

			if source_item in source_list and destination_item in destination_list: #files at both locations -- need to be compared

				command = "less %s %s" % (source_item, destination_item)
				
				if commands.getoutput(command) != "":
					self.source_list.append(source_item)
					self.destination_list.append(destination_item)

			else: #both files don't exist, so they will be copied in the sync

				self.source_list.append(source_item)
				self.destination_list.append(destination_item)










	def _synchronize(self): #this is the last step -- runs the synchronization between the self.source_list and self.destination_list



		for source_item, destination_item in zip(self.source_list, self.destination_list):

			source_name = source_item.replace(self.source, "") #clean the directory from the name
			destination_name = destination_item.replace(self.destination, "") #clean the directory from teh name

			if source_name == destination_name: #just one last validation of the file names
				command = "cp %s %s" % (source_item, destination_item) #create the copy command
				commands.getstatusoutput(command) #actually run the copy of the files




	def _remove(self, file, directory = False):

		# will remove the file that is given -- don't use in development until ready
		command = "rm %s" % file

		commands.getstatusoutput(command)
 


	# PRIVATE METHODS

	def __directory_items(self, directory):

		if directory[-1] == "/":
			directory = directory[:-1]

		command = "find %s" % directory
		results = commands.getoutput(command)

		file_list = results.split()

		return file_list




