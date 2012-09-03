class Configuration:

	def __init__(self, name = "name", source = "source", destination = "destination"):#default constructor
		self.set_name(name).set_source(source).set_destination(destination)
		
	def set_name(self, input_name = "name"):
		self.name = input_name.lower()
		return self
	
	def set_source(self, input_source = "source"):
		self.source = input_source.lower()
		return self	
		
	def set_destination(self, input_destination = "destination"):
		self.destination = input_destination.lower()
		return self
		
# END CLASS
		

	