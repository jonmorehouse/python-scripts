# THIS FILE IS RESPONSIBLE FOR ALL OF THE SETTINGS AND DIRECTORIES FOR DIFFERENT DEPLOYMENT FILES

# WILL ALSO BE RESPONSIBLE FOR QUERYING DB 

class Rip_it_up_world:
	
	static_url = "s3://rip_it_up_world/static"
	static_type = "amazon"
	
	media_url = "s3://rip_it_up_world/media"
	media_type = "amazon"
	
	site_url = ""
	
	local_database = "rip_it_up_world"
	remote_database = "rip_it_up_world"
	
	def __init__(self): #will be responsible for calling the static files and compilation
		# less compilation
		# javascript compilation
		
		

		