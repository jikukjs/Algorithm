def solution(mats, park):
    answer = 0
    col = len(park[0])
    row = len(park)
    now_max = 0
    
    for i in range(row):
        for j in range(col):
            if park[i][j] == "-1":
                posible = []
                for mat in mats:
                    check = 0
                    if (i+mat-1)>=row or (j+mat-1) >= col:
                        continue
                    for x in range(mat):
                        for y in range(mat):
                            if park[i+x][j+y] != "-1":
                                check = 1
                                break
                        if check:
                            break
                    if not check:
                        posible.append(mat)
                if posible:
                    now_max = max(posible)
                #print(now_max)
                if answer < now_max:
                    answer = now_max
    if not answer:
        return -1
                   
    return answer