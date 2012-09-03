1.) input -a (dropbox and other backups that are automated)
 	input -s "source" -d "destination for full"

if -a
2.)	will search for the input in a list, if found then will run the backup command
	if not, will exit and say no automated

3.) if found, will send the source and destination from an array to the backup function

4.) backup function has several functions

	1.) find a list of every single file -- `find . *` in the source
	2.) cd to destination
	3.) check if exists
	4.) if exists, then check if source is newer than destination
	5.) if newer, copy file using source + i and destination + i
	6.) output file changed

