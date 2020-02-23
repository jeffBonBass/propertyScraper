#!/usr/bin/env python

import sys
from lxml import html
import requests
#from BeautifulSoup import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')

def getPropertyValues( pin ):

	#pin = sys.argv[1]
	propertyInfo = []

	url = 'https://taxcommissioner.dekalbcountyga.gov/TaxCommissioner/TCDisplay.asp?ParcelStatus=Y&pin=' + pin
	#url = 'https://taxcommissioner.dekalbcountyga.gov/TaxCommissioner/TCDisplay.asp?ParcelStatus=Y&pin=5180433'
	response = requests.get(url)
	myhtml = response.content
	tree = html.fromstring(myhtml)


	##propertyAddress
	try:
		#address = tree.xpath( '//body/table[2]/tr[2]/td/table/tr/td[1]/table/tr[1]/td/table/tr[4]/td[2]/a/text()' )
		address = tree.xpath( '//body/div/table/tr/td/table/tr/td[1]/table/tr[1]/td/table/tr[4]/td[2]/a/text()' )
		#print( address )
		address = address[0].strip()
		#print(address)
	except IndexError:
		address = ''
	propertyInfo.append( str(address) )


	# neighborhood code
	nbhd = tree.xpath( '//body/div/table/tr/td/table/tr/td[1]/table/tr[6]/td/table/tr[2]/td[2]/text()')
	nbhdCode = nbhd[0]
	#print( nbhdCode )
	propertyInfo.append( str(nbhdCode) )
	
#//body/div/table/tr/td/table/tr/td[1]/table/tr[6]/td/table/tr[4]/td[2]
#//body/div/table/tr
#//body/table[2]/tr[2]

	#improvement type
	myvar = tree.xpath( '//body/div/table/tr/td/table/tr/td[1]/table/tr[6]/td/table/tr[4]/td[2]/text()' )
	imprType = myvar[0].strip()
	#print(imprType)
	propertyInfo.append( str(imprType) )	

	#year built
	myvar = tree.xpath( '//body/div/table/tr/td/table/tr/td[1]/table/tr[6]/td/table/tr[5]/td[2]/text()' )
	yearBuilt = myvar[0].strip()
	#print( yearBuilt )
	propertyInfo.append( str(yearBuilt) )

#//body/div/table/tr/td/table/tr/td[1]/table/tr[6]/td/table/tr[7]/td[2]

	#quality grade
	myvar = tree.xpath( '//body/div/table/tr/td/table/tr/td[1]/table/tr[6]/td/table/tr[7]/td[2]/text()' )
	qualityGrade = myvar[0].strip()
	#print( qualityGrade )
	propertyInfo.append( str(qualityGrade) )

	#air conditioning
	try:
		myvar = tree.xpath( '//body/div/table/tr/td/table/tr/td[1]/table/tr[6]/td/table/tr[8]/td[2]/text()' )
		airConditioning = myvar[0].strip()
		#print( airConditioning )
	except IndexError:
		airConditioning = ''
	propertyInfo.append( str(airConditioning) )

	#square footage
	try:
		myvar = tree.xpath( '//body/div/table/tr/td/table/tr/td[1]/table/tr[6]/td/table/tr[11]/td[2]/text()' )
		squareFootage = myvar[1].strip()
		# just want the square footage value
		sqFt_raw = squareFootage.split()
		squareFootage = sqFt_raw[0]
		#print( squareFootage ):w

	except IndexError:
		squareFootage = ''
	propertyInfo.append( str(squareFootage) )
	
	#bedrooms
	try:
		myvar = tree.xpath( '//body/div/table/tr/td/table/tr/td[1]/table/tr[6]/td/table/tr[14]/td[2]/text()' )
		bedrooms = myvar[0].strip()
		#print( str(bedrooms) )
	except IndexError:
		bedrooms = ''		
	propertyInfo.append( str(bedrooms) )
	
	#bathrooms
	try:
		myvar = tree.xpath( '//body/div/table/tr/td/table/tr/td[1]/table/tr[6]/td/table/tr[15]/td[2]/text()' )
		bathrooms = myvar[0].strip()
		#print( bathrooms)
	except IndexError:
		bathrooms = ''
	propertyInfo.append( str(bathrooms) )
	
	#totalValue
#//body/div/table/tr/td/table/tr/td[1]/table/tr[6]/td/table/tr[23]/td/table/tr[6]/td[2]

	try:
		myvar = tree.xpath( '//body/div/table/tr/td/table/tr/td[1]/table/tr[6]/td/table/tr[23]/td/table/tr[6]/td[2]/text()' )
		totalValue = myvar[0].strip()
		#print( totalValue )
	except IndexError:
		totalValue = ''
	propertyInfo.append( str(totalValue) )
	
	#appeal?
# if exists -> appeal
#//body/div/table/tr/td/table/tr/td[1]/table/tr[6]/td/table/tr[23]/td/table/tr[8]/td[2]

	myvar = tree.xpath( '//body/div/table/tr/td/table/tr/td[1]/table/tr[6]/td/table/tr[23]/td/table/tr[8]/td[2]' )
	#print(myvar)
	if len(myvar) > 0:
		appeal = "YES"
		#print( "Appeal: Yes" )
	else:
		appeal = "NO"
		#print( "Appeal: No" )

	propertyInfo.append( str(appeal) )
	
	# variables
	# bathrooms, bedrooms, squareFootage, airConditioning, qualityGrade, yearBuilt, nbhdCode, imprType, address, totalValue
	# create a tab-delimited record
	propRecord = address + '\t' + yearBuilt + '\t' + imprType + '\t' + nbhdCode + '\t' + qualityGrade + '\t' + airConditioning + '\t' + squareFootage + '\t' + bedrooms + '\t' + bathrooms + '\t' + totalValue + '\t' + appeal
	print(propRecord)
	return propertyInfo

if __name__ == '__main__':
    pin  = sys.argv[1]
    #print( str.format(pin) )
    getPropertyValues( pin )
