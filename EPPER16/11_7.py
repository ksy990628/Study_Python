def solution(n,arr):
    arr.sort()
    for i in range(n-1):
        arr[i+1] = (arr[i]+arr[i+1])/2

    return arr[n-1]





print(solution(3,[1,3,5]))
