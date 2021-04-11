def solution(left,right):

    if left == 0 and right == 0:
        return 1

    else:
        if left == 0: #왼쪽 괄호를 다 쓴 상태로, 오른쪽만 사용 가능
            return 1
        elif left < right: #오른쪽 괄호가 왼쪽 괄호보다 많은 경우
            return solution(left-1,right)+solution(left,right-1)
        else: #왼쪽 괄호 == 오른쪽 괄호
            return solution(left-1,right)
            



    return result


print(solution(1,1))
