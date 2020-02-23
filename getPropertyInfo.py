#!/usr/bin/env python

import sys
from lxml import html
import requests
import mechanize
from getPropertyPins import getPropertyPins
from scrape import getPropertyValues

# input: street name to search against
# call getPropertyPins.py -> returns tab-delimited list of pins and street addresses
# create a list with pins/addresses
# pass list into scrape program
# receive list/tab-delimted output?
# todo: tweak street list

#def getPropertyInfo( streetName ):

propertyValues = []
if len( sys.argv ) < 2:
	print "Usage: getPropertyInfo <street name>"
else:
	#print sys.argv[1]
	pinList = []
	pinList = getPropertyPins( sys.argv[1])
	print 'PinList has ' + str(len(pinList)) + ' entries.'
	print pinList

	for pin in pinList:
		print "Pin: " + str( pin[0] )
		propertyValues.append( getPropertyValues( pin[0] ) )
	print propertyValues

	#write values to file (probably should make that part of the above processing
	print "...saving to file...\n"
	for value in propertyValues:
		print value
		with open( "./street_" + sys.argv[1] + ".txt", 'a' ) as f:
			f.write( '\t'.join( value ) + '\n' )

