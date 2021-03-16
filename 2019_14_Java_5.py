def solution(n,m,word,start):
    word.sort()
    num_word = []
    for i in range(n):
        num_word.append(0)

    #print(word)
    #print(num_word)


    for i in range(m):
        tmp = []
        for j in range(n):
            if start[i] == word[j][0]:
                tmp.append(j)
                #print(word[j])
                
        min = 100000
        min_obj = 0
        #빈도수 최소인 것 가리기 == min_obj 빈도수 최소인 인덱스 
        for k in tmp:
            if num_word[k] < min:
                min = num_word[k]
                min_obj = k
                        
        print(word[min_obj])
        num_word[min_obj] +=1
        #print(num_word)



print(solution(4,5,['zagreb','split','zadar','sisak'],['z','s','s','z','z']))
#print(solution(5,3,['london','rim','pariz','moskva','sarajevo'],['p','r','p']))
solution(1,3,['zagreb'],['z','z','z'])    
