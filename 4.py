#!/usr/bin/env python3
# http://www.pythonchallenge.com/pc/def/linkedlist.php

from re import search
from urllib.request import urlopen

#id = 12345
id = 92118/2
while True:
	response = urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d' % id)
	line = response.read()
	print(line)
	#id = int(line[-5:])
	id = int(search(r'\d+$', str(line, encoding='utf8')).group(0))
