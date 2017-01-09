#!/usr/bin/python

import sys
import urllib

urlconstloc = 'http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22'
sOutFile = 'rt22.xml'

#open url location.. returns an xml file
def ReadData(urlloc,outfile):
	try:
		u=urllib.urlopen(urlloc)
		data = u.read()
		fhand = open(outfile,'wb')
		fhand.write(data)
		fhand.close()
		print(fhand)
	except:
		print error
		print(fhand)
def main():
	argnum = len(sys.argv)
	print 'Number of arguments:',argnum,'arguments.'
	print 'Argument List:', str(sys.argv)
	if argnum > 1:
		ReadData(sys.argv[1],sOutFile)
	else:
		ReadData(urlconstloc,sOutFile)

if __name__ =='__main__':
	main()
