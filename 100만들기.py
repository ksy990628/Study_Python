def solution(tmp):
    total = sum(tmp)

    for i in range(len(tmp)):
        for j in range(i+1,len(tmp)):
            if total-tmp[i]-tmp[j] == 100:
                tmp.remove(tmp[j])
                tmp.remove(tmp[i])
                return tmp


print(solution([1 ,3 ,4, 5 ,15, 30, 42, 61, 72]))
