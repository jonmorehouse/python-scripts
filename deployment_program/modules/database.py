import utilities, commands, time





# this class is responsible for backing up the database -- will be used to run bash commands and generate proper file names etc

class Database(object):

	local_name = "asdfasf"

	def __init__(self, configuration):

		

		self.configuration = configuration
		self.file_name()



	def file_name(self): #this function is responsible for creating the properly formatted file_name

		# check if file exists (if it does, need to change the file name to add a (1) on the end)
		
		current_time = time.strftime('%m_%d_%H_%M')
		name = "%sdatabase/%s.sql" 
		self.local_name = "%sdatabase/%s.sql" %(self.configuration.get("local_archive"), current_time)
		self.live_name = "%sdatabase/%s.sql" %(self.configuration.get("live_archive"), current_time)

		return self


	def local_dump(self): #will dump the local database into the project../archives/database/folder

		# MAKE DIR IF DOESN'T EXIST

		credentials = dict()
		credentials['username'] = self.configuration.get("username")
		credentials['password'] = self.configuration.get("password")
		credentials['host'] = "localhost"
		credentials['database'] = self.configuration.get("local_database")

		utilities.bash.mysql_dump(credentials, self.local_name)

		return self
		

	def dump_live_database(self):pass #will be responsible for dumping the live database -- can be reused -- maybe make this a module to add in later


		












