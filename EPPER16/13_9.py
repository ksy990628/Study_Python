def solution(n,arr):
    dp = [0]*n
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(dp[0]+arr[2],dp[1],arr[1]+arr[2])
    
    for i in range(3,n):
        dp[i] = max(dp[i-2]+arr[i],dp[i-3]+arr[i-1]+arr[i],dp[i-1])
    
    return dp[n-1]

print(solution(8, [5, 7, 10, 1, 2, 10, 10, 8]))
print(solution(8, [1, 2, 3, 4, 5, 6, 7, 8]))