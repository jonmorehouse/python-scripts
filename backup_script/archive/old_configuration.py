backups = []
source = []
destination = []

backups.append("desktop")
source.append("~/Desktop/source")
destination.append("~/Desktop/destination")

backups.append("hello world")

def valid_command(command):
	if command in valid_command:
		return true
	else:
		return false
		
def get_source(command):
	if command in backups:
		position = backups.index(command)
	return source[position]