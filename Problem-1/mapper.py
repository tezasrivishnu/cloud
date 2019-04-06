#!/usr/bin/env python

import sys
import json

def mapper(inp):
	key = inp[0]
	value = inp[1].strip()
	words = value.split()
	seen = {}
	for i in words:
		inter = {}
		if (not seen.get(i,False)):
			seen[i]	= True
			inter.setdefault(i, [])
			inter[i].append(key)
			print i, inter[i]

for i in sys.stdin:
			inp = json.loads(i)
			mapper(inp)


