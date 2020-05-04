maze = [
    ['a','b','c','d','e'], # row 0
    ['f','g','h','i','m'], # row 1
    ['k','u','c','n','a'], # row 2
    ['p','t','a','s','t'], # row 3
    ['u','v','r','x','y'], # row 4
]
crosswords=[
        [0,0],[1,1],[2,2],[3,3],[4,4],
        [0,1],[1,2],[2,3],[3,4],
        [0,2],[1,3],[1,4],
        [0,3],[1,4],
        [0,4],
        [1,0],[2,1],[3,2],[4,3],
        [1,1],[2,2],[3,3],[4,4],
        [1,2],[1,3],[1,4],
        [1,3],[1,4],
        [1,4],
    ]

MAX_COLS=5
MAX_ROWS=5
words = ['car','can','him','mat','gut','tame','tug','big']
cols = []
for i in range (len(maze[0])):
    c=[]
    for j in range (len(maze)):
        c += [maze[j][i]]
    cols += [c]    
    cols += [list(reversed(c)) ]   
print (cols)
#exit()

for word in words:
    for m in range(len(maze)):
        #print(''.join(maze[m]))
        if word in ''.join(maze[m]):
            print("found",word)

    for m in range(len(cols)):
        if word in ''.join(cols[m]):
            print("found",word)

