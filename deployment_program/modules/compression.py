# THIS CLASS IS RESPONSIBLE FOR HANDLING THE COMBINATION OF MULTIPLE FILES TOGETHER 
from utilities import bash, general
from utilities.mysql import Mysql

class Compression(object):
	
	def __init__(self, configuration):
		
		self.configuration = configuration
		self.mysql = Mysql(configuration.get("local_database"))
				
	
	
	def _compress(self):#will get the files and combine them accordingly -- need to get the unique types
		
		rows = self.mysql.unique(self.table, "page_id") #get the unique pages in this site
		page_ids = []
		
		for row in rows:
			page_ids.append(row['page_id'])
		
		# ACTUALLY GATHER THE FILES FOR EACH ONE
		for page_id in page_ids:
			
			# for each page_id that is distinct, need to create a file -- means that we gather all relevant files and put them in order and compile
			
			url = self._url(page_id) #this is the file name that will be the output of all the orders
			ordered_list = self._ordered_list(page_id) #generate the file_list in order
			

			self._combine(ordered_list, url) #this will combine and compress the files using yui compresssor (no less compilation)
			self.__update(page_id, url) #this will update the database with the proper url and will 'deactivate other files'
			
												
		return True
		# create the file from the file list
		# update the database with this information -- need to query the old one!
		# Actually run the combine file command
		
	
		
	def _ordered_list(self, page_id):
		
		file_list = self.mysql.where("page_id", page_id).where("status", False).get(self.table) #generate the total list
		ordered_list = []
		
		for _file in file_list:
			ordered_list.append(_file['url'])
		
		if len(ordered_list) == 0:
			return False
		
		return ordered_list
			
		
	
	# 		END OF METHOD -- USED FOR VANILLA FILE FINDING
				
	def _combine(self, ordered_list, url): #send this the "raw list of objects" and it will put them in the proper order and cat them
		

		directory = general.slash(self.configuration.get("static_directory"))
		
		file_name = directory + url
		file_paths = []
			
		for item in ordered_list:

			path = directory + item['url']
			file_paths.append(path)
			
		# NOW CONCATENATE ALL THE FILES:
		
		bash.combine(file_name, file_paths)
		bash.compress(file_name)
		
		return file_name #this is the name that the file was saved and compressed to
			
	
	
	def __update(self, page_id, url): #will be responsible for updating the database so that we are responsible for this new file!
		
		# this is going to take out the "live/" from the url so that it works okay with database systems

		url = url.replace("live/", "")


		# DELETE ANY OTHER LIVE FILES IN THE DB -- (UNLINK THEM!)
		self.mysql.where("status", True).where("page_id", page_id).delete(self.table)


		# NOW INSERT WITH THE NEW NAME
		columns = ["page_id", "url", "status"] #columns for this particular site setup
		values = [page_id, url, True,]#values for this particular site setup

		# TAKE CARE OF THE CSS/JS SPECIFIC VALUES FOR THE TABLE
		for i in self.columns:
			columns.append(i)
		for i in self.values:
			values.append(i)

		self.mysql.insert(self.table, values, columns) #the database is now update properly
	
	
	def __url(self):pass #this is replaced in the child class
		
	
		
		