import os.path, commands
from utilities import backup




# THIS CLASS WILL BE RESPONSIBLE FOR BACKING UP FILES TO THE AMAZON S3 SERVER

	


class Amazon(backup.Backup):

	def __init__(self, source, destination, public = False):

		self.amazon = False

		self.public = public
		
		if super(Amazon, self).__init__(source, destination):

	 		if self.__is_amazon(source) or self.__is_amazon(destination):
 				self.amazon = True
	 			self._backup() #run the sync because there's an amazon s3 folder present

 			else: #both vanilla directories locally!
 			 	super(Amazon, self)._backup()


	
	def __is_amazon(self, directory):

		amazon = directory.find("s3://")

		if amazon != -1: #means that the s3 was found in the directory
			return True

		else:
			return False


	def _backup(self):

		if not self.amazon:
			super(Amazon, self)._backup()

		else: #this is the section to run the amazon synchronization

			if self.source[-1] != "/":
				self.source = self.source + "/"

			if self.destination[-1] != "/":
				self.destination = self.destination + "/"


			self.synchronize()

	def synchronize(self): #this is the synchronization for amazon server 


		command = "s3cmd sync %s %s" % (self.source, self.destination)
		output = commands.getoutput(command) #actually synchronize the files!

		if (self.public): #the acl settings need to be true! -- need to pass in the public folder as the third one -- just to be safe

			print "Now setting acl-public for %s" % self.public
			command = "s3cmd setacl --acl-public --recursive %s" % self.public
			commands.getoutput(command)



	# check whether a file is the same
	def _exists(self, directory):

		if self.__is_amazon(directory): #we can verify that this is an amazon directory
			return True

		# if not __is_amazon, we still need to check if it is a local directory

		else: #this directory is localized
			return super(Amazon, self)._exists(directory)

