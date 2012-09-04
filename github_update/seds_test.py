#!/usr/bin/python

from classes import cleaner

import os, json

with open('configuration.json') as configuration:
    configuration = json.load(configuration)

test_file = "~/Desktop/test_seds.txt"

cleaner.Cleaner(configuration['credentials'])

file_credentials = configuration['projects'][0]['credentials']

file_cleaner = cleaner.File_cleaner(file_credentials)

file_cleaner.clean_file(test_file)
