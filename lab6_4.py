# 빵이 한 번에 한 개 나올 때
bread = 10

while bread > 0 :
    money = int(input('돈을 넣어주세요 : '))
    if money < 500:
        print('빵을 사기에 금액이 부족합니다.')
    else:  #money >= 500
        bread -= 1
        print("빵을 받으세요.")
        if money - 500 > 0:
            print("거스름돈 ",money - 500,"원이 나옵니다.")
        print("남은 빵의 개수는 %d 개 입니다." %bread)




# 입력한 금액의 최대치로 빵이 나올 
'''
bread = 10
money = int(input('돈을 넣어주세요 : '))
if money < 500:
    print('금액이 부족합니다.')
else:  #money >= 500
    bread = bread - money/500
    print(int(money/500),"개의 빵이 나옵니다.")
    print("남은 빵의 개수는 %d 개 입니다." %bread)
    print("거스름돈 ",money%500,"원이 나옵니다.")
    
'''
