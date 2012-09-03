import os # import the system -- allows you to run any command you want with bash
import commands # commands.getoutput() allows you to get the command output
import sys # allow python to grab the argument
import string
import configuration
import helper
import backup
import options

from configuration import *
from options import *

# MODULES ARE FOR FUNCTIONS
# CLASSES ARE FOR STORING DATA!



selection = sys.argv[1]

if selection.lower() != "all":
	for i in range(len(backups)):
		if backups[i].name.lower() == selection:
			backup.main(i)
else:
	for i in range(len(backups)):
		backup.main(i)
		






