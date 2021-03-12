#점수 4개 중 상위 3개의 점수 평균을 구하는 함수
def average(score1,score2,score3,score4):

    #점수가 0과 100 사이의 수가 아닌 경우 함수 종
    if score1 < 0 or score1 >100:
        print("invalid parameter")
        return
    elif score2 < 0 or score2 > 100:
        print("invalid parameter")
        return
    elif score3 < 0 or score3 > 100:
        print("invalid parameter")
        return
    elif score4 < 0 or score4 > 100:
        print("invalid parameter")
        return

    #상위 3개의 점수 평균을 구하기 위해 점수값 내림차순으로 정렬
    score_list = [score1,score2,score3,score4]
    score_list.sort()
    score_list.reverse()

    #상위 3개의 점수 총합 계산
    sum = 0
    for i in range(0,3):
        sum += score_list[i]
    result = sum / 3

    '''
    if score1 < score2 and score1 < score3 and score1 < score4:
        result = (score2+score3+score4)/3
    elif score2 < score1 and score2 < score3 and score2 < score4:
        result = (score1+score3+score4)/3
    elif score3 < score1 and score3 < score2 and score3 < score4:
        result = (score1+score2+score4)/3
    elif score4 < score1 and score4 < score2 and score4 < score3:
        result = (score1+score2+score3)/3
    '''
    return result



