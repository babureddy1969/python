#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
'''
chocolates=10
cost = 2
wrappers=5 per chocolate

chocolates  wrappers    total 
10          0           10
0           10
5           0           5
0           5           
2           1           2
0           3           
1           1           1
0           2
1           0           1
0           1           


'''

c=10
cpc=2
c=c/cpc
wpc=5
w=c
while  w >= wpc:
    count=w/wpc
    w = count+(w % wpc)
    c += count
print (int(c))