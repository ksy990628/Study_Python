def solution(n):
    room = n // 15 + 1
    num = n % 15
    
    if n % 15 == 0:
        room = n // 15 
        num = 15

    result = str(room) + " " + str(num)
    print(result)

solution(7)
solution(16)
solution(30)