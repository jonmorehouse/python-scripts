# this class is responsible for going to the proper directory, pushing the application
# this class is responsible for downloading live data from dotcloud
# this class is responsible for uploading a local dump as well
import commands

class Dotcloud(object):

	def __init__(self, local_dump, configuration, update = False):

		# local_dump is the file that needs to be uploaded to the dotcloud server
		# configuration is used for accessing different directories etc
		self.configuration = configuration
		self.update = update

		self.upload_to_dotcloud(local_dump)

		if update:
			self.update_on_dotcloud()

		self.sync_dotcloud()
		self.push_dotcloud()



	def upload_to_dotcloud(self, local_url):

		print "Now uploading local database to Dotcloud"
		command = "cd %s && dotcloud run %s.db \"cat > data.sql\" < %s" % (self.configuration.dotcloud_directory, self.configuration.dotcloud_name, local_url)

		commands.getoutput(command) #run the upload of the data 




	def download_from_dotcloud(self):pass


		# command = "cd %s %% dotcloud run %s.db \" mysqldump -u%s -p%s %s > live_dumps/data.sql"



	def update_on_dotcloud(self): #update the database on dotcloud

		print "Now updating the dotcloud database with local information"
		command = "cd %s && dotcloud run %s.db \"mysql -u%s -p%s %s < data.sql\"" % (self.configuration.dotcloud_directory, self.configuration.dotcloud_name, self.configuration.username, self.configuration.password, self.configuration.remote_database)

		commands.getoutput(command)
		# dotcloud run ripitupworld.db "mysql -uMorehouseJ09 -pMoeller12 rip_it_up_world < data.sql"

	def sync_dotcloud(self):

		print "Synchronizing the local project files with the dotcloud files -- only responsible for apps"

		for app in self.configuration.app_list:

			source = self.configuration.site_directory + app
			destination = self.configuration.dotcloud_directory + app

			command = "cp -r %s %s" % (source, destination)
			commands.getoutput(command)





	def push_dotcloud(self):


		print "Pushing code to dotcloud server"

		command = "cd %s && dotcloud push %s" % (self.configuration.dotcloud_directory, self.configuration.dotcloud_name)
		commands.getoutput(command)
		




# dotcloud run ripitupworld.db "cat > data.sql" < ../archive/database/09_02_12_30.sql
