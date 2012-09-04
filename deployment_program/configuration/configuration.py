from utilities.mysql import Mysql
from modules import css, database, javascript, amazon



class Configuration(object):
	
	def __init__(self):
		self.mysql = Mysql(self.database)
		
	def get(self, item):


		if (item == "static_url"):
			return self.static_url
		
		elif (item == "static_type"):
			return self.static_type
			
		elif (item == "media_url"):
			return self.media_url
			
		elif (item == "media_type"):
			return self.media_type
		
		elif (item == "site_url"):
			return self.site_url
			
		elif (item == "site_type" or item == "server"):
			return self.server
			
		elif (item == "local_database"):
			return self.local_database

		elif (item == "remote_database" or item == "live_database"): 
			return self.remote_database
		
		elif (item == "local_archive"):
			return self.local_archive
			
		elif (item == "live_archive"):
			return self.live_archive
				
		elif (item == "static_directory"):
			return self.static_directory #this is the actual location on the local machine -- with absolutes!
			
		elif (item == "media_directory"):
			return self.media_directory
			
		elif (item == "site_directory"):
			return self.site_directory
		
		elif (item == "password"):
			return self.password

		elif (item == "username"):
			return self.username
	
	
		
	def javascript(self):#will be responsible for compiling the javascript and saving it to the db / local storage
		
		print "Now compiling and compressing javascript files for %s" % self.project_name
		javascript.Javascript(self)
	
		
	
	
	def css(self):#will be responsible for compiling the css and saving it to the db/local storage
		
		print "Now compiling and compressing css files for %s" % self.project_name
		css.Css(self)
	
	
	def database(self):

		print "Now backing up databases for %s" % self.project_name

		database_backup = database.Database(self)
		database_backup.local_dump()

		return database_backup.local_name




	

