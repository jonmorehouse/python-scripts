#!/usr/bin/python


import classes.github

configuration = dict()
configuration['path'] = "/Users/MorehouseJ09/Documents/github/prospero"
configuration['message'] = "test message"
configuration['repo'] = "Prospero"


c = classes.github.Github(configuration)
c.update()