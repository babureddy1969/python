def findType():
 c=input()
 found=False
 try:
     c=int(c)
     print ('This input is of type Integer.',end='')
     found=True
 except:
     pass
 if not found:
  try:
     c=float(c)
     print ('This input is of type float.',end='')
     found=True
  except:
     pass
 if not found:
  try:     
     print ('This input is of type string.',end='')
     found=True
  except:
     pass
