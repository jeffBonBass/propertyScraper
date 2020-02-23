#!/usr/bin/env python

import sys
from lxml import html
import requests
import mechanize

def getPropertyPins( streetName ):

	url = r'https://taxcommissioner.dekalbcountyga.gov/TaxCommissioner/TCSearch.asp'
	request = mechanize.Request(url)
	response = mechanize.urlopen(request)
	forms = mechanize.ParseResponse(response, backwards_compat=False)
	response.close()

	form = forms[0]

	form['StreetName']=sys.argv[1]
	propertyList = mechanize.urlopen(form.click()).read()

	tree = html.fromstring(propertyList)
	pins = tree.xpath( '//tr/td[1]/a/@href' )
	addresses = tree.xpath( '//tr/td[1]/a/text()' )

	pinList = []
	i = 0
	for pin in pins:
		#print pin
		newpin = pin.split('=')
		pinList.append( [ newpin[3], addresses[i] ] )
		print newpin[3] + '\t' + addresses[i]
		i = i + 1
	
	return pinList

if __name__ == '__main__':
    streetName  = sys.argv[1]
    getPropertyPins( streetName )
