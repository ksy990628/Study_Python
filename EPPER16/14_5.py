def solution(n,m,word,start):
    word.sort()
    num_word = [0]*n
    for i in range(m): #입력받은 첫 알파벳
        tmp = []
        for j in range(n):  #단어들 중에 알파벳과 일치하는 것이 있는 지 확인
            if start[i] == word[j][0]:
                tmp.append(j)
                #print(word[j])                
        min = 100000 #최소값인지 개수 세기
        min_obj = 0  #해당 단어 인덱스
        #빈도수 최소인 것 가리기 == min_obj 빈도수 최소인 인덱스 
        for k in tmp:
            if num_word[k] < min:
                min = num_word[k]
                min_obj = k
                        
        print(word[min_obj])
        num_word[min_obj] +=1

solution(4,5,['zagreb','split','zadar','sisak'],['z','s','s','z','z'])
solution(5,3,['london','rim','pariz','moskva','sarajevo'],['p','r','p'])
solution(1,3,['zagreb'],['z','z','z'])    