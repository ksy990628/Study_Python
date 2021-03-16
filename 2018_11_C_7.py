def solution(n,arr):
    arr.sort()
    avg = 0

    if len(arr) == 1:
        return arr[0]
    
    for i in range(len(arr)-1):
        arr[i+1] = (arr[i]+arr[i+1])/2
        if i == len(arr)-2:
            avg = arr[i+1]
    return avg
    



print(solution(1,[3]))
