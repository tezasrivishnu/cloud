#!/usr/bin/env python
import sys
import json

inter = {}
def mapper(inp):

	id_ = inp[1]
	inter.setdefault(id_, [])
	inter[id_] = inp
	print id_, inter[id_]

for i in sys.stdin:
	inp = json.loads(i)
	mapper(inp)