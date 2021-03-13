def solution(m,n):
    change = m - n
    
    m10000 = change // 10000
    m5000 = change % 10000 // 5000
    m1000 = change % 5000 // 1000
    m500 = change % 1000 // 500
    m100 = change % 500 // 100
    m50 = change % 100 // 50
    m10 = change % 50 // 10

    money = [m10000,m5000,m1000,m500,m100,m50,m10]
    kind = 0
    for i in range(len(money)):
        if money[i] > 0:
            kind+=1

    result = str(kind)+" "+str(sum(money))

    return result



print(solution(10000,8240))
