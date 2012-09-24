#!/usr/bin/python

import sys, commands

youtube_link = sys.argv[1]

temp_directory = "/Users/MorehouseJ09/music_downloads/"
youtube_command = "youtube-dl --extract-audio --audio-format mp3 -o \"%%(title)s.mp3\" %s" % youtube_link

command = "cd %s && %s" % (temp_directory, youtube_command)

commands.getoutput(command)

