#!/usr/bin/env python
import sys
import json

def mapper(inp):
	print inp[0], inp[1]

for i in sys.stdin:
	inp = json.loads(i)
	mapper(inp)
