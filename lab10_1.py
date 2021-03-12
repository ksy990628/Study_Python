#전역변수 
PI = 3.14159

#원의 면적(지역변수)
def circle_area(r):
    result = PI * r * r
    return result


#원의 둘레(지역변수)
def circle_circumference(r):
    result = 2 * PI * r
    return result


#전역변수 r (radius)
r = float(input('원의 반지름: '))
print('원의 면적: ', circle_area(r))
print('원의 둘레: ', circle_circumference(r))
