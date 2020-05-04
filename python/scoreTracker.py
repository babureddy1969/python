#scorecard
def breakingRecords(scores):
    up=0
    down=0
    for i in range(len(scores)):
        if i<len(scores) and scores[i] < scores[i+1]:
            up+=1
        elif i<len(scores) and scores[i] > scores[i+1]:
            down+=1
    return up,down