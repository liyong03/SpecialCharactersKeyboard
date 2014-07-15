#!/usr/bin/python

import urllib2
from bs4 import BeautifulSoup
import json
import os
import subprocess
import codecs

charsList = []

print "Get all symbol list ..."
page = urllib2.urlopen("http://fsymbols.com/all/")
soup = BeautifulSoup(page)
symbolContainers = soup.body.find_all('table', attrs={"class": "sym"})
#print symbolContainers
for symbols in symbolContainers:
	th = symbols.find_all("th")
	name = ""
	if len(th):
		name = th[0].string
		print name
	contents = [x.string for x in symbols.find_all("td")]
	contents = filter(None, contents)
	contents = [x.encode('utf-8') for x in contents]
	for x in contents:
		print x 
	print contents
	print "============="
	obj = {}
	obj["name"] = name
	obj["contents"] = contents
	charsList.append(obj)

f = codecs.open("./chars.json", "w", "utf-8")
json.dump(charsList, f)
f.close()
