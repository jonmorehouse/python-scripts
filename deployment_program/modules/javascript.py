import compression, utilities


class Javascript(compression.Compression):#this is an object that is responsible for getting site information and compiling information--pass it a configuration object
	
	def __init__(self, configuration):
		
		super(Javascript, self).__init__(configuration)
		
		self.table = "header_javascript" #javascript header information file
				
		self.columns = ["js_type"] #used for updating the header_javascript table
		self.values = ["live"] #used for updating the header_javascript table
		
		
		self._compress()
	
			
		
	def _url(self, page_id): #this is used to generate the custom url
		
		if page_id == "all":
			name = "site_wide"
		
		else:
			name = page_id

		return "javascript/live/%s.js" % name
	
	# END CLASS JAVASCRIPT
	
	
	# CUSTOM JAVASCRIPT ORDERING -- THESE CAN ALL BE REPLACED IN THE FUTURE
	def _ordered_list(self, page_id):#this program will be responsible for compiling for each page_id
		
		files = self.mysql.where("status", False).where("page_id", page_id).select(["url", "js_type"]).get(self.table)
		
		
		if files: #the files exist == need to sort them
			
			ordered_files = []
			site_wide = []
			utilities = []
			modules = []
			pages = []
			other = []
			
			for _file in files:
				if _file['js_type'] == "site_wide":
					site_wide.append(_file)
				
				elif _file['js_type'] == "utilities":
					utilities.append(_file)
				
				elif _file['js_type'] == "modules":
					modules.append(_file)
				
				elif _file['js_type'] == "pages":
					pages.append(_file)
				
				elif _file['js_type'] != "live":
					other.append(_file)
			whole_list = [site_wide, utilities, modules, pages, other]
			
			for _list in whole_list:

				ordered_files.extend(_list)
	
			return ordered_files
					
				
		else:
			return False


		
#END OF OBJECT
	
	


	
	
	
	
	
	
