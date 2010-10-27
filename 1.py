#!/usr/bin/env python3
# http://www.pythonchallenge.com/pc/def/map.html

# k -> m    11 -> 13
# o -> q    15 -> 17
# e -> g     5 ->  7

#text = 'koe'
#text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
text = "map"
translated = []
for character in list(text):
	if 'a' <= character < 'y':
		translated.append(chr(ord(character)+2))
	elif character == 'y':
		translated.append('a')
	elif character == 'z':
		translated.append('b')
	else:
		translated.append(character)
print(''.join(translated))
