import commands

# NOTE THIS CLASS IS PRIMARILY FOR UPDATING TO GITHUB
# CAN CREATE EASY RULES FOR CUSTOM GITHUB CONFIGURATIONS BY EXTENDING THIS GITHUB CLASS
# CAN USE A CONFIG SETTING IF NECESSARY FOR THIS 

class Github(object):

	
	def __init__(self, configuration):

		self.configuration = configuration #this has all of the github features for this particular commit


	def update(self):

		self._add() #add all the files to the relevant git commit
		self._commit_message() #generate the proper git message
		self._commit() #generate a commit through the terminal
		self._push() #push the code


	def _add(self):

		command = "cd %s && git add *" % self.configuration['path'] #add all of the files to the github commit

		commands.getoutput(command)

		return self


	def _commit_message(self):

		prompt = "Please input a commit message for %s: \n" % self.configuration['repo']
		message = raw_input(prompt) 

		if len(message) == 0:
			self.message = self.configuration['message'] #use the default message

		else:
			self.message = message #the message validates properly

		return self

	def _commit(self):

		command = "cd %s && git commit -am \" %s \"" % (self.configuration['path'], self.message)
		commands.getoutput(command)

		return self

	def _push(self):

		command = "cd %s && git push -u origin master" % self.configuration['path']

		print commands.getoutput(command)

		return self



