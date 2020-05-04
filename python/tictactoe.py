#tic tac toe
problem = [
    [1,0,2],
    [0,2,0],
    [2,0,1]
]
cols = [
    [problem[0][0],problem[1][0],problem[2][0]],
    [problem[0][1],problem[1][1],problem[2][1]],
    [problem[0][2],problem[1][2],problem[2][2]]
    ]

for col in cols:
    if len(set(col)) == 1:
        print(col, ' is valid')

for row in problem:
    if len(set(row)) == 1:
        print(row, ' is valid')
r=[]
col=0
for row in range(0,3):
    r += [problem[row][col]]
    col += 1
if len(set(r)) == 1:
    print('diagnol 1 is valid', r)


r=[]
col=0
for row in range(2,-1,-1):
    r += [problem[row][col]]
    col += 1
if len(set(r)) == 1:
    print('diagnol 2 is valid', r)





solutions=[
    [1,1,1],
    [2,2,2]
]
rows=[]
for r in range (3):
    row=[]
    for c in range(3):
        row += [problem[r][c]]
    rows += [row]
#print(rows)
cols=[]
for c in range (3):
    col=[]
    for r in range(3):
        col += [problem[r][c]]
    cols += [col]
#print(cols)
cross=[]
c=0
x=[]
for r in range (3):
    x += [problem[r][c]]
    c += 1
    if c == 2:
        cross += [x]
c=2
x=[]
for r in range (3):
    x += [problem[r][c]]
    c -= 1
    if c == -1:
        cross += [x]
        break
#print(cross)
#exit(0)
player = 1
while True:
    #print (problem)
    print('----------')
    for i in range(0,3):
        for j in range (0,3):
            print (problem[i][j],end='\t')
        print('\n')
    print('----------')
    s = "Player "+str(player)+ ", enter Row and Column:"
    r, c = eval(input(s)) 
    r = int(r)
    c = int(c)
    if problem[r][c] == 0:
        problem[r][c] = player
    if player == 1: 
        player = 2
    elif player == 2:
        player = 1
    for i in range(3):
        if all(rows[i]):
            s = set(rows[i])
            if s =={1}:
                print("Player 1 wins")
                exit()
            if s =={2}:
                print("Player 2 wins")
                exit()
        if all(cols[i]):
            s = set(cols[i])
            if s =={1}:
                print("Player 1 wins")
                exit()
            if s =={2}:
                print("Player 2 wins")
                exit()
        if i<2 and all(cross[i]):
            s = set(cross[i])
            if s =={1}:
                print("Player 1 wins")
                exit()
            if s =={2}:
                print("Player 2 wins")
                exit()
