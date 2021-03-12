score = int(input('점수를 입력하시오: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:   #60점 미만 elif score < 60:
    grade = 'F'

print('학점은 %s 입니다.' %grade)






'''
score = int(input('점수를 입력하시오: '))
if (score>=60):
    if (score>=70):
        if (score>=80):
            if (score>=90):
                grade = 'A'
            else:
                grade = 'B'
        else:
            grade = 'C'
    else:
        grade = 'D'
else:
    grade = 'F'

print('학점은 %s 입니다.' %grade)
'''
