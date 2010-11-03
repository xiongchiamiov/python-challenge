#!/usr/bin/env python3
# http://www.pythonchallenge.com/pc/def/peak.html
# Had to get a hint in the forums about this one. Spent a week trying to figure
# out where to go from 'Yes, pickle!' >_>

import pickle
from pprint import pprint
from urllib.request import urlopen

response = urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
data = pickle.load(response)
#pprint(data)
#
#print('-' * 80)
#
#for l in data:
#	print(sum((i[1] for i in l)))
#
#print('-' * 80)

for l in data:
	for t in l:
		print(t[0]*t[1], end='')
	print()
