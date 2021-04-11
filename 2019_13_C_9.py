def solution(n,arr):
    dp1 = 0
    dp2 = 0

    for i in range(n):
        if arr[i]+arr[i+1] > dp2:
            dp2 = arr



print(solution(8,[5,7,10,1,2,10,10,8])
