row, column = map(int, input().split())
grape =[]
row_n = 0
column_n = 0

for _ in range(row):
    row_l = list(input())
    if 'X' not in row_l:
       row_n+=1 
    grape.append(row_l)

for j in range(column):
    check = 1
    for i in range(row):
        if grape[i][j] == 'X':
            check = 0
            break
    if check:
        column_n +=1

print(max(row_n,column_n))
    