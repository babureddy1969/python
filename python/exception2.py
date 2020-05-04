import sys
try:
    import xyz as r
except ModuleNotFoundError as m:
    import random as r
    print(m)
try:
    f = open('x.csv')
    f.read()
except FileNotFoundError as a:
    print(sys.exc_info()[1],"File does not exist")
except ValueError as a:
    print(sys.exc_info()[1],'Cannot read file after closing')
finally:
    print('finally block')
    try:
        f.close()
    except NameError as n:
        pass