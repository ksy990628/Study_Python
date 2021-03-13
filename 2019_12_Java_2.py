def solution(n):
    room = 0
    number = 0
    
    if n % 15 == 0:
        room = int(n/15)
        number = 15
    else:
        room = int(n/15) + 1
        number = n % 15

    answer = str(room) + " "+ str(number)

    return answer



print(solution(30))
