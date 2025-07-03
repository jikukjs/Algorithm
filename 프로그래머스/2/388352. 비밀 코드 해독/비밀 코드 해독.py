from itertools import combinations

def solution(n, q, ans):
    answer = 0
    candidates =[]
    num_list = []
    
    for i in range(1, n+1):
        num_list.append(i)
    
    for i in range(len(q)):
        if ans[i] == 0:

            num_list = list(set(num_list)- set(q[i]))
        
        if ans[i] == 5 :
            answer = 1
            return answer
            
#     def DSF(idx, n_list):
#         if idx == len(num_list):
#             if len(n_list) == 5:
#                 candidates.append(n_list[:])
#             return
#         n_list.append(num_list[idx])
#         DSF(idx+1,n_list)
#         n_list.pop()
#         DSF(idx+1,n_list)
    
#     DSF(0,[])
    
#    for candidate in candidates:
    for candidate in combinations(num_list, 5):
        check = 0
        for i in range(len(q)):
            if len(set(q[i]) & set(candidate)) != ans[i]:
                check = 1
                break
        if not check:
            answer+=1    
    
    return answer