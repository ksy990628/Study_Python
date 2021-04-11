def solution(n,m,arr):
    day = 0
    not_tomato = 0
    row = []
    column = []

    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                not_tomato += 1
            elif arr[i][j] == 1:
                row.append(i)
                column.append(j)
                
    #print(not_tomato)

    while not_tomato > 0:
        change = False
        day += 1
        for k in range(len(row)):
            i = row.pop()
            j = column.pop()
            change = changeTomato(i,j,arr,not_tomato,row,column,m,n)
            
        if change == False:
            break

    if not_tomato == 0:
        return day
    else:
        return -1

def changeTomato(i,j,arr,not_tomato,row,column,m,n):
    change = False
    
    if i != 0 and arr[i-1][j] == 0: #위쪽
        arr[i-1][j] = 1
        not_tomato -= 1
        row.append(i-1)
        column.append(j)
        change = True
        
    if j != n - 1 and arr[i][j+1] == 0: #오른쪽
        arr[i][j+1] = 1
        not_tomato -= 1
        row.append(i)
        column.append(j+1)                
        change = True
        
    if i != m - 1 and arr[i+1][j] == 0: #아래쪽
        arr[i+1][j] = 1
        not_tomato -= 1
        row.append(i+1)
        column.append(j)                
        change = True
        
    if j != 0 and arr[i][j-1] == 0: #왼쪽
        arr[i][j-1] = 1
        not_tomato -= 1
        row.append(i)
        column.append(j-1)
        change = True
        
    print(arr)
    return change

print(solution(6,4,[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,1]]))
