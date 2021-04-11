def solution(m,arr):
    number = [0,1,2,3,4,5,6,7,8,9]
    operator = ['+','-','*','/']
    result = []

    for i in range(0,m):
        if (arr[i] in number):
            result.append(arr[i])
            
        elif(arr[i] in operator):
            t2 = result.pop()
            t1 = result.pop()
            
            if arr[i] == '+':
                result.append(t1+t2)
            elif arr[i] == '-':
                result.append(t1-t2)
            elif arr[i] == '*':
                result.append(t1*t2)
            elif arr[i] == '/':
                result.append(abs(t1//t2))
            #print(result[len(result)-1])
    return result[0]

print(solution(3,[2,3,'+']))
print(solution(3,[4,1,'-']))
print(solution(3,[9,4,'/']))
print(solution(7,[2, 3, '+', 2, '*', 2, '/']))
print(solution(11,[9, 8, '/', 4, '-', 5, '*', 2, '+', 3,'*']))
print(solution(11,[2, 3, 4, '*', '+' ,5 ,'/', 6, 7, '+', '-']))
print(solution(5,[1, 2, 3, '*', '+']))                
# 5 3 2 5 -39 -11 7