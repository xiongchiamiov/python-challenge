#!/usr/bin/env python3
# http://www.pythonchallenge.com/pc/def/channel.html

from zipfile import ZipFile
z = ZipFile('channel.zip')

num = 90052 # From channel/readme.txt
while True:
	zi = z.getinfo('%s.txt' % num)
	print(zi.comment.decode('ascii'), end='')
	f = open('channel/%s.txt' % num, 'r')
	line = f.readline()
	# print(line)
	# I don't know what the last one'll look like, so just try to keep going
	# and we'll use the output and ignore the exception at the end.
	num = line.split()[3]
