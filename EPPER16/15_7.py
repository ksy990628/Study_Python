#도서관 좌석 예약
def solution(s,e):
    tmp = [0] * len(s)
    for i in range(len(s)):
        tmp[i] = [s[i],e[i]]
    tmp.sort(key = lambda x : x[1])
    print(tmp)
    e1 = -1
    e2 = -1    
    count = 0
    
    for i in range(len(s)):
        if e1 <= tmp[i][0]:
            count += 1
            e1 = tmp[i][1]
        elif e2 <= tmp[i][0]:
            count += 1
            e2 = e1
            e1  = tmp[i][1]
    
    return count 
            
print(solution([0,6,3,1,1,2],[3,7,10,5,9,8])) 
print(solution([845, 26921, 15116, 1694, 43588],
               [64754, 32669, 57396, 8835, 50160]))