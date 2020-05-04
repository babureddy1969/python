'''feb=28
julian_calendar_min=1700
julian_calendar_max=1917
y=1700
#y=2016
if y>=julian_calendar_min and y<=julian_calendar_max and y%4 == 0 :
    feb = 29
elif y>=1919 and ( y%400 == 0 or (y%4 ==0 and y%100 !=0)):
    feb = 29
months={1:31,2:feb,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
days=0
day256=256
month=1
for k,v in months.items():
    if day256 - days>29:
        days+=v
        month = k
    else:
        break
month+=1
d=day256-days
print ('{:02d}.{:02d}.{:4d}'.format(d,month,y))'''

def getDate(year):
    if (year == 1918):
        return '26.09.1918'
    elif ((year <= 1917) & (year%4 == 0)) or ((year > 1918) & (year%400 == 0 or ((year%4 == 0) & (year%100 != 0)))):
        return '12.09.%s' %year
    else:
        return '13.09.%s' %year
 