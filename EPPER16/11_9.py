#괄호 문제

def solution(left,right):
    if left == 0 and right == 0:
        return 1
    
    else:
        if left == 0:
             return 1
        elif left < right:
             return solution(left-1,right)+solution(left,right-1)
        else: #left == right
             return solution(left-1,right)
    
    
    
print(solution(1,1))
print(solution(2,2))
print(solution(3,3))