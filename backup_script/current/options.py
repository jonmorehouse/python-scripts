import configuration
import string

from configuration import *

backups = []
backups.append(Configuration("desktop", "~/Desktop/source", "~Desktop/destination"))
backups.append(Configuration("desktop_test", "~/Desktop/source_test", "~Desktop/source_destination"))
