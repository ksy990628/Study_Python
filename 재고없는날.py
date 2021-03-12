def solution(n,m):
    total = n
    day = 0
    while total > 0:
        day += 1
        total -= 1
        if day % m == 0:
            total += 1

    return day
    







print(solution(7,2))
