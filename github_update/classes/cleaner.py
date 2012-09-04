import commands


class Cleaner(object): 

	credentials = [] #to be used between different projects
	
	temp_file = "/tmp/github_update/temporary_clean/temp"

	banned_file_types = []

	def __init__(self, credentials, file_types): #credentials is a list of dicts that hold the value and replacements of all words that should be removed

		self.credentials.extend(credentials)

		for item in file_types:

			self.banned_file_types.append(item.lower())


class File_cleaner(Cleaner):


	def __init__(self, credentials): #to be used for an individual project

		self.file_credentials = []
		self.file_credentials.extend(self.credentials) #extend the local file credentials with the parent's credentials (as found in configuration['credentials'])
		self.file_credentials.extend(credentials) #extend the local file credentials with the given credentials

	def clean_file(self, path):#

		if self.__valid_file(path):
			# this object is responsible for looping through all of the credentials and cleaning this individual file!
			command = "sed "

			for file_credential in self.file_credentials:
				replacement = file_credential['replacement'].replace(" ", "")
				command += "-e s/%s/%s/g " % (file_credential['value'], replacement)

			command += "%s > %s && mv %s %s" % (path, self.temp_file, self.temp_file, path) #output to the temp file and move the temp file to the proper place

			commands.getoutput(command) #actually run the substitution for this individual file -- not too efficient but it is simplistic for just working locally

	def __valid_file(self, path):

		extension = path.split(".")[-1]

		if extension.lower() in self.banned_file_types:

			return False

		else:
			return True



