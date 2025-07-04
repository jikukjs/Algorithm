from itertools import combinations

def solution(clothes):
    answer = 0
    clothes_type = set()
    clothes_hash = {}
    clothes_list = []
    for cloth in clothes:
        clothes_type.add(cloth[1])
        if cloth[1] not in clothes_hash.keys():
            clothes_hash[cloth[1]] = 1
        else:
            clothes_hash[cloth[1]]+=1
    sum_ = 1
    for i in clothes_hash.values(): 
        sum_ *= (i+1)
        
    
    return sum_-1