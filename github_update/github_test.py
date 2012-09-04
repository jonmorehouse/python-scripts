#!/usr/bin/python


import classes.github

configuration = dict()
configuration['path'] = "/Users/DefaultPassword/Documents/github/prospero"
configuration['message'] = "test message"
configuration['repo'] = "Prospero"


c = classes.github.Github(configuration)
c.update()
