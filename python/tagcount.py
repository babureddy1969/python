import urllib.request, urllib.parse, urllib.error
#from urllib import request, parse, error 
from bs4 import BeautifulSoup

#url="https://github.com/grantjenks/python-wordsegment"
url="http://en.wikipedia.org/wiki/Conversion_of_units_of_temperature"
html = urllib.request.urlopen(url).read()
# json
#url="https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson" 
dict={}
bs=BeautifulSoup(html, "lxml")
print(bs.title())
print('divs:',len(bs.find_all('div')))
print('ul:',len(bs.find_all('ul')))
print('li:',len(bs.find_all('li')))
print('meta:',len(bs.find_all('meta')))
print('span:',len(bs.find_all('span')))
print('button:',len(bs.find_all('button')))
print('links:',len(bs.find_all('a')))
a = bs.find_all('a')
href=0
for x in a:
	if 'href' in x.attrs.keys():
		href += 1
print('href:',href)
