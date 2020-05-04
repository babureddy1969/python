f= open('mail.txt')
for line in f:
    line = line.rstrip()
    if 'uct.ac.za' not in line:
        print(line)