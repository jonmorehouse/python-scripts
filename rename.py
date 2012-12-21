#!/usr/bin/python

#future functionality
#add recursive feature -- to do this recursively

import os

for i in os.listdir("."):

	name = i.replace(" ", "_").replace("-","_").lower()
	os.rename(i,name)
	


