def avg():
    x = int(input('정수 1을 입력하세요: '))
    if x < 0 or x > 100:
        print("잘못된 입력입니다.")
        return 
    y = int(input('정수 2을 입력하세요: '))
    if y < 0 or y > 100:
        print("잘못된 입력입니다.")
        return 
    return (x+y)/2
