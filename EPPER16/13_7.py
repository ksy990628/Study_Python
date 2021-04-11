def solution(n,arr):
    time = 0
    for i in range(len(arr)//2):
        if arr[i] != arr[len(arr)-1]:
            arr[i+1] = arr[i]+arr[i+1]
            arr.pop(i)
            time += 1
            
    return time

print(solution(3,[1,2,3]))
print(solution(5,[1,2,4,6,1]))
print(solution(4,[1,4,3,2]))