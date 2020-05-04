import urllib.request, urllib.parse, urllib.error
#from urllib import request, parse, error 
from bs4 import BeautifulSoup
import ssl
import pandas as pd
from collections import OrderedDict
from pandas import ExcelWriter
from pandas import ExcelFile

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url="http://stats.espncricinfo.com/ci/engine/player/28081.html?class=2;template=results;type=batting;view=innings"
html = urllib.request.urlopen(url, context=ctx).read()

temp_data=OrderedDict()
list_of_dict=[]
bs=BeautifulSoup(html, "lxml")
table_body=bs.find_all('tbody')
rows = table_body[1].find_all('tr')
for row in rows:
    cols=row.find_all('td')
    cols=[x.text.strip() for x in cols]
    temp_data=OrderedDict()
    for i in range(len(cols)):
    	temp_data["Runs"]=cols[0]
    	temp_data["Mins"]=cols[1]
    	temp_data["BF"]=cols[2]
    	temp_data["4s"]=cols[3]
    	temp_data["6s"]=cols[4]
    	temp_data["SR"]=cols[5]
    	temp_data["POS"]=cols[6]
    	temp_data["Dismissal"]=cols[7]
    	temp_data["Inns"]=cols[8]
    	temp_data["Opposition"]=cols[10]
    	temp_data["Ground"]	=cols[11]
    	temp_data["Date"]=cols[12]
    list_of_dict.append(temp_data)
	
df=pd.DataFrame(list_of_dict)
print(df)