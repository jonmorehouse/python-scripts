import commands, os, time



# FOR FILE LIST -- WE NEED TO NORMALIZE NAMES, PATHS AND BANNED NAMES
# RELIES ON THE FACT THAT DIRECTORIES ARE GIVEN WITHOUT TRAILING SLASHES -- MAKES IT EASEIER TO USE FIND



class File_list(object):

	# SHARE ATTRIBUTES GO HERE -- OBJECTS THAT ARE VARIABLES SHARED BETWEEN ALL INSTANCES OF A CLASS

	def __init__(self, directory, banned_files = [], banned_directories = []):

		self.banned_files = banned_files #banned files for this file
		self.file_list = [] # this is the file list
		self.banned_directories = []

		for banned_directory in banned_directories: #normalize all the banned directories for this object
			self.banned_directories.append(self.__normalize_slashes(banned_directory))


		self.directory = self.__normalize_slashes(directory) #plain directory to be used throughout


	# PUBLIC METHODS

	def get_file_list(self):

		self._files() #will add the plain files to the file_list

		for directory in self._directories():

				self._recursive_files(directory) #this will add all of the files from each of the directories into the file list

		for item in self.file_list:

			item["directory"] = self.directory

		# WE NOW HAVE THE FILES INTO THE FILE LIST

		return self

	def clean_file_list(self):

		_file_list = self.file_list

		self.file_list = []

		for item in _file_list:

			flag = True #this file is allowed until this is false

			for banned_item in self.banned_files:

				if item['name'] == banned_item: #if the names are the same -- does not matter on path because the directory could be different -- source v destination
					flag = False

					break
			# FINISHED LOOPING THROUGH BANNED LOOP
			if flag: #add this to the new file_list

				self.file_list.append(item) #add it back to the file_list

		# END OF FOR LOOP FOR ITEMS IN FILE LIST

		return self


	# PROTECTED METHODS

	def _directories(self):#this function will return all the directories that are in this parent directory -- will make sure not in the banned_list

		command = "ls -l %s | grep \"d\" | awk '{print $9}'" % self.directory #command that lists all the directories in the folder given -- but not any hidden directories!

		directories = commands.getoutput(command).split() #get the actual directories -- test this for type later -- does not append a slash
 			
 		verified_directories = []

		for directory in directories:

			if os.path.isdir(self.directory + "/" + directory) and directory not in self.banned_directories: #check that the directory is actually a directory
				verified_directories.append(directory)

		return verified_directories #return this to the calling function

	def _files(self):#this function is responsible for just getting the files in the top level directory

		command = "ls -l %s | grep ^- | awk '{print $9}'" % self.directory

		files = commands.getoutput(command).split() #get a list of all the files that are in this directory

		for item in files: #loop through each file and ensure that you are addin the correct name and path

			directory_file = dict()
			directory_file['name'] = item
			directory_file['path'] = self.directory + "/" + item

			self.file_list.append(directory_file) #append to the list


	# PRIVATE METHODS

	def _recursive_files(self, directory): #this function is useful for recursively getting the files in a directory and adding them to the file_list

		relative_directory = directory
		absolute_directory = self.directory + "/" + directory #remember that self.directory does  -- this is the full path!
		
		command = "cd %s && find . -type f | grep \"./\"" % absolute_directory #get only the files -- this is used to exclude just the dot

		files = commands.getoutput(command).split()


		for item in files:

			directory_file = dict()
			directory_file['name'] = relative_directory + "/" + item.replace("./", "")
			directory_file['path'] = self.directory + "/" + directory_file['name']

			self.file_list.append(directory_file)

		return self


	def __normalize_slashes(self, directory):

		if directory[-1:] == "/": #realize that teh : means range so this means the range after -1 until the end
			directory = directory[:-1] #means range before -1

		return directory


class File_synchronization(object):#this object is responsible for the overall synchronization -- lets keep these objects maintained		

		
	def __init__(self, source_list, destination_list, directories, project_name = "Default"):#this class is responsible for synchronizing files between the source and destination

		self.deleted_files = []
		self.synchronization_list = []
		self.source_list = source_list #please note that these are cleansed full path urls
		self.destination_list = destination_list #please note that these are cleansed full path urls
		self.project_name = project_name

		self.source_directory = directories['source']
		self.destination_directory = directories['destination']

		self.__mk_trash() #create the trashcan for this synchronization

	# PUBLIC METHODS

	def synchronize(self):

		self._clean_destination() #delete any files that need to be deleted from teh destination
		self._synchronization_list() #create the synchronization list

		for item in self.synchronization_list: #loop through the synchronization list that was created before

			self.__copy_file(item)

		return self #return self so that users can use the deleted items list if need


	# PROTECTED METHODS


	def _clean_destination(self):#will go through each of the files in the destination and see if they are in the source, if not they are moved to the trash

		for item in self.destination_list:#loop through each destination file

			flag = False

			for source_item in self.source_list: #loop through each source_item

				if item['name'] == source_item['name']:
					flag = True #the file is valid -- it can stay

			if not flag: #have looped through all of the source items and the destination file name is not one of them

				self.__delete(item) #mark the file for deletion

		return self

		# END OF METHOD FOR CLEANING THE DESTINATIONS


	def _synchronization_list(self): #will loop through the source and destination files and will then compare the paths using the less command

		# this is going to loop through the source, find the name of the same item in the other folder and will then compare the two files using less
		for source_item in self.source_list:

			flag = False

			for destination_item in self.destination_list:

				if destination_item['name'] == source_item['name']:#ensure that both file_names are the same, if so, then we need to run this 
				
					flag = True
	
					if not self.__compare(source_item['path'], destination_item['path']): #this is the the comparison function

						sync = dict()
						sync['source'] = source_item['path']
						sync['destination'] = destination_item['path']

						self.synchronization_list.append(sync)

				if flag: #stop looping through the destination items -- this source item was already found
					break #break loop

			# END OF DESTINATION FOR LOOP -- STILL LOOPING THROUGH SOURCE LIST

			if not flag: #the item is not in the destination directory -- need to add it

				sync = dict()
				sync['source'] = source_item['path']
				sync['destination'] = self.destination_directory + "/" + source_item["name"]

				self.synchronization_list.append(sync) # add to our global list

		# END OF FOR LOOP FOR SOURCE ITEMS

		return self



	# PRIVATE METHODS

	def __compare(self, file_1, file_2): #this program is going to take in two files and will return true if they are the same, false if not

		command = "diff %s %s"  % (file_1, file_2) 

		diff = commands.getoutput(command)

		if len(diff) > 0: #the files are differnet

			return False #signal that the files are different

		else: 
			return True

	def __copy_file(self, item): #this expects to see a source and item as a 'dict' -- need to create directory trees

			file_name = item['destination'].split("/")[-1]

			directory = item['destination'].replace(file_name, "") #create teh directory now!

			command = "mkdir -p %s" % directory #create the directory

			commands.getoutput(command) #create the directory tree!
			command = "cp %s %s" % (item['source'], item['destination']) #create the command
			commands.getoutput(command) #copy the file over

	def __mk_trash(self): #this function is responsible for making the trash directory -- a temp folder for this directory

			current_time = time.strftime('%m_%d_%H_%M')

			folder_name = "%s_%s" % (self.project_name, current_time)

			url = "/tmp/github_update/%s/" % folder_name #url for the trash

			command = "mkdir -p %s" % url #this is the command to create the trash directory 

			commands.getoutput(command) #create the directory!

			self.trash_directory = url

			return self

	def __delete(self, item):

		command = "mv %s %s" % (item['path'], self.trash_directory)

		commands.getoutput(command) #this file is now moved to the trash bin

		deleted_file = dict()
		deleted_file['name'] = item['name']
		deleted_file['path'] = self.trash_directory + item['name']

		self.deleted_files.append(deleted_file)

		return self

