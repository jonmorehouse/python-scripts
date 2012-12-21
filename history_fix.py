#!/usr/bin/python

file_name = "/Users/MorehouseJ09/.bash_history"

commands = []


with open(file_name) as raw_history:

	for i in raw_history:

		i = i.strip()

		if not i in commands:
			commands.append(i)

raw_history.closed #true the file is closed

with open(file_name, "w") as writer:

	writer.write("")

with open(file_name, "a") as writer:

	for i in commands:
		writer.write(i + '\n')






