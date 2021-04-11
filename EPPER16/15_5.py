def solution(case):
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    result = ''
    tmp = 0
    if case[0] == '1':
        result += '1'

    for i in range(len(case)-1):
        if case[i] == case[i+1] and i == len(case)-2:
            tmp += 1
            result += str(alpha[tmp])
            
        elif case[i] == case[i+1]:
            tmp += 1
        
        if case[i] != case[i+1] and i == len(case)-2 :
            result += str(alpha[tmp])
            result += str(alpha[0])
            
        elif case[i] != case[i+1]:
            result += str(alpha[tmp])
            tmp = 0

    return result


print(solution("000"))
print(solution("11111"))
print(solution("00011110"))
print(solution("111100100011"))
