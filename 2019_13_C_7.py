def solution(n,arr):
    result = 0
    if n % 2 == 1:
        round = n // 2 + 1
    else:
        round = n // 2
        
    for i in range(round):
        if arr[i] != arr[n-i-1]:
            arr[i] = arr[i]+arr[i+1]
            arr.remove(arr[i+1])
            result += 1

    return result


print(solution(5,[1,2,4,6,1]))
