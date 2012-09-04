# THIS FILE IS RESPONSIBLE FOR ALL OF THE SETTINGS AND DIRECTORIES FOR DIFFERENT DEPLOYMENT FILES
from configuration import Configuration
from utilities.mysql import Mysql
from modules import amazon, dotcloud


# WILL ALSO BE RESPONSIBLE FOR QUERYING DB 

class Rip_it_up_world(Configuration):
	
	amazon_url = 's3://rip_it_up_world/'

	static_url = 's3://rip_it_up_world/static/'
	static_type = 'amazon'
	static_directory = '/Users/DefaultPassword/Documents/production_development/rip_it_up_world/current/static/'
	
	media_url = 's3://rip_it_up_world/media/'
	media_type = 'amazon'
	media_directory = '/Users/DefaultPassword/Documents/production_development/rip_it_up_world/media/'
	
	site_url = 'http://ripitupworld-DefaultPassword.dotcloud.com/'
	site_directory = '/Users/DefaultPassword/Documents/production_development/rip_it_up_world/current/'
	server = 'dotcloud'
		
	local_database = 'rip_it_up_world'
	remote_database = 'rip_it_up_world'
	
	local_archive = '/Users/DefaultPassword/Documents/production_development/rip_it_up_world/archive/' #local archive -- assuming 
	live_archive = 's3://rip_it_up_world/archive/'

	username = 'DefaultPassword'
	password = 'DefaultPassword'
	
	site_status = False
	project_name = "RipItUpWorld"

	dotcloud_directory = '/Users/DefaultPassword/Documents/production_development/rip_it_up_world/dotcloud/'
	dotcloud_name = "ripitupworld"

	
	def __init__(self):
			
		self.javascript() #if there is custom javascript just extend this class and 'over-ride the parent function!'
		self.css() #this function is responsible for compiling the less into one css file
		
		# RUN THE DATABASE HERE SO THE DUMP CAN BE UPLOADED!
		dump_file_name = self.database() #this section is responsible for dumping the datbase and backing it up to the proper file
		
		# will be responsible for copying files over and then pushing to dotcloud as well as pushing the new database live

		self.dotcloud(dump_file_name) #will push any files and will then upload any database dumps and will download the live database dumps

		self.amazon() #run the amazon section -- updates amazon s3 server after we have downloaded everything

		# THIS WILL RUN THE ENTIRE THING
		# 1.) Generate CSS
		# 2.) Generate Javascript
			
	def amazon(self):
		# this section is responsible for backing up the different folders to the correct locations for amazon deployment

		backups = dict()

		# backup any media items that could be needed
		backups['media'] = dict()
		backups['media']['source'] = self.media_directory
		backups['media']['destination'] = self.amazon_url + "media/"
		backups['media']['public'] = self.amazon_url + "media/" 

		# copy the javascript files into the site javascript to be served
		backups['javascript'] = dict()
		backups['javascript']['source'] = self.static_directory + "javascript/live/"
		backups['javascript']['destination'] = self.amazon_url + "static/javascript/"
		backups['javascript']['public'] = self.amazon_url + "static/javascript/"


		# copy the css files into the site css to be served
		backups['css'] = dict()
		backups['css']['source'] = self.static_directory + "css/live/"
		backups['css']['destination'] = self.amazon_url + "static/css/"
		backups['css']['public'] = self.amazon_url + "static/css/"

		# backup the code base
		backups['code_base'] = dict()
		backups['code_base']['source'] =  self.site_directory
		backups['code_base']['destination'] = self.amazon_url + "archives/code_base/"
		backups['code_base']['public'] = False

		# upload the archive folder of this local project
		backups['archives'] = dict()
		backups['archives']['source'] = self.local_archive
		backups['archives']['destination'] = self.amazon_url + "archives/local_archives/"
		backups['archives']['public'] = False

		# download live website dumps 
		backups['live_dumps'] = dict()
		backups['live_dumps']['source'] = self.amazon_url + "archives/live_dumps/"
		backups['live_dumps']['destination'] = "/Users/DefaultPassword/Documents/production_development/rip_it_up_world/live_data/"
		backups['live_dumps']['public'] = False


		for name in backups:
			backup = backups[name]
			amazon.Amazon(backup['source'], backup['destination'], backup['public'])

	def dotcloud(self, file_name):


		self.app_list = ["ajax_sessions/", "content/", "header/", "blog/", "success_stories/", "templates/"]
		dotcloud.Dotcloud(file_name, self, True)









		



