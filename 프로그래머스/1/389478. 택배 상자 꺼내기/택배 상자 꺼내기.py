def solution(n, w, num):
    answer = 0
    storage = []
    n_list = []
    left = -1
    
    for i in range(n):
        n_list.append(i)
        if len(n_list) == w:
            if left == 1:
                n_list.reverse()
            storage.append(n_list)
            n_list = []
            left = left*(-1)
    
    while(len(n_list) != w):
        n_list.append(0)
    if left == 1:
        n_list.reverse()
    storage.append(n_list)
    
    num_row = (num-1)//w
    num_col = storage[num_row].index(num-1)
    
    print(len(storage)-1)
    
    if storage[len(storage)-1][num_col] == 0:
        answer = len(storage)-num_row -1
    else :
        answer = len(storage)-num_row 
    
    print(storage)
    print(num_row,num_col)
        
    return answer