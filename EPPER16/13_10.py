cnt = [0,0]*26     #알파벳 개수를 저장
dp = [-1]*(1<<16)

def calc_pref(n,x):
    len = 0 #중복 알파벳 개수
    temp = [0]*26
    for i in range(26):
        temp[i] = 999999
    for i in range(n):
        if ((x & (1 << i)) != 0): # 문자열 포함 확인
            for j in range(26):
                if temp[j] > cnt[i][j]:
                    temp[j] = cnt[i][j]
                else:
                    temp[j] = temp[j]
    len = sum(temp)
    return len

def solve(n,x):
    # 이전 결과 활용
    if (dp[x] != -1) :
        return dp[x];
    
    # 문자열 조합 x에서 모두 중복되는 알파벳 개수 연산
    pref = calc_pref(n, x);
    # x가 2의 제곱수인지 확인
    # =>문자열 1개만 포함한 조합
    # 해당 문자열 개수 반환

    if ((x&-x) == x):
        dp[x] = pref
        return dp[x]
    # 모든 문자열 조합 모두 순회
    dp[x] = 999999;
    for i in range((x-1)&x, 0, (i-1)&x):
        curr = solve(n, i) + solve(n, x^i) - pref
        if (dp[x] > curr):
            dp[x] = curr
        else:
            dp[x] = dp[x]
    return dp[x];


def solution(n,arr):
    for i in range(len(arr)):
        cnt[i] = len(arr[i])
    return solve(n, (1<<n)-1) + 1    
    
# 4 4 5
print(solution(3,['a','ab','abc'])) 
print(solution(3,['a','ab','c']))
print(solution(4,['baab','abab','aabb','bbaa']))