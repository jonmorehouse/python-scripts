#!/usr/bin/python
import json, urllib2

try:

	with open("config.json", "r") as rawJson:

		# 
		config = json.loads(rawJson.read())

except Exception, e:

	print e
	exit()


def encodeUserData(user, password):
    return "Basic " + (user + ":" + password).encode("base64").rstrip()

#
url = 'https://api.github.com/users/%s/repos' % (config['username'])
req = urllib2.Request(url)


connection = 
headers = {
	
	"Accept" : "application/json",
	"Content": "application/x-www-form-urlencoded",
	"Authorization" : encodeUserData(config['username'], config['password']),

}

data = {
	

	


}

h.request('POST', url, data, headers)

# make the request
response = request.getresponse()

print res.read()



