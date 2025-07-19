T = int(input())

for _ in range(T):
    password = input()
    stack_1 = []
    stack_2 = []
    
    for w in password:
        if w == "<":
            if stack_1:
                temp = stack_1.pop()
                stack_2.append(temp)

        elif w == ">":
            if stack_2:
                temp = stack_2.pop()
                stack_1.append(temp)
        
        elif w == "-":
            if stack_1:
                stack_1.pop()
                        
        else :
            stack_1.append(w)
        
    stack_1.extend(reversed(stack_2)) 
    print("".join(stack_1))        