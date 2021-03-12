def solution(tmp):
    result = ""
    if tmp[0] == "1":
        result += "1"
        
    count = 0
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    for i in range(len(tmp)-1):
        
        if i == len(tmp)-2:
            if tmp[i] == tmp[i+1]:
                count += 1
                result += (alpha[count])
                count = 0
            else:
                result += (alpha[count])
                count = 0
                result += alpha[0]

        elif tmp[i] == tmp[i+1]:
            count += 1

        else:
            result += (alpha[count])
            count = 0

    
    return result
        

print(solution("00000000000000000000010000000011111111111111000000"))
