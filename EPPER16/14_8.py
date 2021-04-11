def check(i,j,m,n):
    if i < 0 or j < 0:
        return False
    if i >= m or j >= n:
        return False
    return True
    
#주변 토마토를 익히고, 새롭게 익은 토마토는 다음 queue에 담기.
def changeTomato(notTomato,x,y,newGoodTomato,m,n,arr):
    pos = [[-1,0],[1,0],[0,-1],[0,1]]
    for i in range(len(pos)):
        newX = x + pos[i][0] # -1 1 0 0
        newY = y + pos[i][1] #  0 0 -1 1
        if check(newX,newY,m,n) and arr[newX][newY] == 0:
            arr[newX][newY] = 1
            newGoodTomato.append([newX,newY])
            notTomato -= 1
    return arr,notTomato,newGoodTomato


def solution(n,m,arr):
    notTomato = 0
    goodTomato = []
    newGoodTomato = [] 
    tmp = []
    days = 1
 
    #안 익은 토마토와 이미 익은 토마토 구분
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                notTomato += 1
            elif arr[i][j]  == 1:
                goodTomato.append([i,j])

    #토마토 익히기 시작
    while True:
        if notTomato == 0:
            break
        
        #goodTomato에 있는 토마토로 주변 토마토를 익히고, 새롭게 익은 토마토는 newGoodTomato에 담는다
        for i in range(len(goodTomato)):
            arr,notTomato,newGoodTomato = changeTomato(notTomato,goodTomato[i][0],goodTomato[i][1],newGoodTomato,m,n,arr)
        
        #새롭게 익은 토마토가 없다면, 토마토가 모두 익지 못하는 상황.
        if len(newGoodTomato) == 0:
            break
 
        days += 1
        #q2를 q1으로 옮기고, q2는 비운다.
        tmp = goodTomato
        goodTomato = newGoodTomato
        newGoodTomato = tmp
        newGoodTomato.clear()
        

        print(arr)
        print(notTomato)
        print(goodTomato)
        print(newGoodTomato)


    #최종 결과 출력
    if notTomato == 0:
        return days-1
    else:
        return -1

#print(solution(6,4,[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,1]]))
#print(solution(6,4,[[0,-1,0,0,0,0],[-1,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,1]]))
print(solution(5,5,[[-1,1,0,0,0],[0,-1,-1,-1,0],[0,-1,-1,-1,0],[0,-1,-1,-1,0],[0,0,0,0,0]]))



'''
n, m = 5, 5
n_list = [[-1, 1, 0, 0, 0], [0, -1, -1, -1, 0], [0, -1, -1, -1, 0], [0, -1, -1, -1, 0], [0, 0, 0, 0, 0]]
non_ri_tomato = 0
ri_tomato = []
vecX = [1, -1, 0, 0]
vecY = [0, 0, -1, 1]

for i in range(m):
    for j in range(n):
        if n_list[i][j] == 0:
            non_ri_tomato += 1
        if n_list[i][j] == 1:
            new_ri_tomato = [i, j]
            ri_tomato.append(new_ri_tomato)
            
while(ri_tomato):
    now_tomato = ri_tomato.pop(0)
    for i in range(4):
        nowX = now_tomato[0] + vecX[i]
        nowY = now_tomato[1] + vecY[i]
        if(nowX >= 0 and nowX < m and nowY >= 0 and nowY < n):
            if n_list[nowX][nowY] == 0:
                n_list[nowX][nowY] = n_list[now_tomato[0]][now_tomato[1]] + 1
                new_ri_tomato = [nowX, nowY]
                ri_tomato.append(new_ri_tomato)
                non_ri_tomato -= 1

if non_ri_tomato == 0:
    print(n_list[now_tomato[0]][now_tomato[1]]-1)
else:
    print(-1)
'''