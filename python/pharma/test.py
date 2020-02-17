data={}
products={}
with open('product.csv') as product:
    for line in product.readlines()[1:]:
        line = line.split(',')
        products[line[0]] = {'name':line[1],'unit_price':line[2]}
with open('sale.csv') as sale:
    for line in sale.readlines()[1:]:
        s=line.split(',')
        x=s[2].split('-')
        dt=x[0]+x[1]+x[2].split()[0]+'|'+s[1]
        data[dt] = data.get(dt,0) + int(s[3])*int(products[s[1]]['unit_price'])
agg=[]
final={}
for k,v in data.items(): 
    agg+=[(v,k)]
agg.sort()

        
print(data)