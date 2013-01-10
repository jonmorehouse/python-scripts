#!/usr/bin/python

import json

try:

	with open("config.json", "r") as rawJson:
		config = json.loads(rawJson)

except Exception, e:

	print e
	raise e

print config
