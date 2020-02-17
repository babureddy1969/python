from bs4 import BeautifulSoup
html = None
with open('Mobile_telephone_numbering.html',encoding='utf8') as f:
    html=f.read()
bs=BeautifulSoup(html, "lxml")
td = bs.find_all('td')
with open('out.csv','w') as o:
    for d in td:
        o.write(d.text+',')