import compression, utilities

class Css(compression.Compression):
	
	def __init__(self, configuration):
		
		super(Css, self).__init__(configuration)
		
		self.table = "header_style_sheets"
		
		self.columns = ["file_type"]
		self.values = ["stylesheet"]
		
		self._compress()
			
	
	
	def _url(self, page_id):#this function is going to be used to overwrite the parent method that is also used to deploy
		
		if page_id == "all":
			name = "site_wide"
		else:
			name = page_id
				
		url = "css/live/%s.css" % name
				
		return url
		
			
	
	
	# this function is a replacement combination for the parent class -- because this is different than the parent
	def _combine(self, ordered_list, url):#this function is responsible for running the conversion / concatenation for the css system
		
		self.directory = utilities.general.slash(self.configuration.get("static_directory"))



		# FIRST, we need to copy all files to a temp folder
		# next we need to convert each one (using the sh)
		# finally, combine all of those files into the last one
		counter = 1
		temp_directory = "%scss/.tmp/" % (self.directory)

		utilities.bash.mkdir(temp_directory)

		for item in ordered_list:
						
			input_file = "%s%s" % (self.directory, item)
			output_file = "%s%s.css" % (temp_directory, counter)
			
			utilities.bash.less_compile(input_file, output_file)
			counter += 1


		url = self.directory + url

		utilities.bash.folder_combine(temp_directory, url)
		
		utilities.bash.rmdir(temp_directory)

		utilities.bash.compress(url)


		




		 
		
		
		
			
		
	
	
		
	
	
	
	

	