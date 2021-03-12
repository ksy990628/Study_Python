'''
# 비어있는 리스트를 확인할 수 있는 코드
a = []
if not a: # true
    print('a is empty!')
'''
def solution(n,arr1,arr2):
    #a = map(int,input().split())
    s1=[]
    s2=[]
    total = 2
    
    for i in range(0,86400):
        s1.append(0)
        s2.append(0)

    for i in range(0,n):
        start = arr1[i]
        end = arr2[i]
        flag1 = True
        flag2 = True
            
        for k in range(start,end):
            if s1[k] == 1:
                flag1 = False
            if s2[k] == 1:
                flag2 = False
                    
        if flag1==False and flag2==False:
            total += 1
        else:
            if flag1 == True:
                for k in range(start,end):
                    s1[k] = 1
            elif flag1 == False and flag2 == True:
                for k in range(start,end):
                    s2[k] = 1
    return total
        
#print(solution(2,[0,2],[2,4]))
print(solution(6,[0,6,3,1,1,2],[3,7,10,5,9,8]))
