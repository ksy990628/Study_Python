N, R = map(int, input().split())
n = list(map(int, input().split()))
r = []
for i in range(R):
   r.append(list(map(int, input().split())))
goal = int(input())

# 초기 배열 3개 설정!
adj = [[0]*101 for _ in range(101)]
indgree = [0] * 101
time = [0] * 101

queue = []
for i in range(0, R):
    u = r[i][0]
    v = r[i][1]
    adj[u][v] = 1;
    indgree[v] += 1;
    
for i in range(1, N+1):
    if(indgree[i] == 0):
        time[i] = n[i-1]
        queue.append(i)

while(queue):
    now = queue.pop(0)
    for i in range(1, N+1):
        if(adj[now][i] == 1):
            time[i] = max(time[i], time[now] + n[i-1])
            indgree[i] -= 1
            if(indgree[i] == 0):
                queue.append(i)
print(time[goal])