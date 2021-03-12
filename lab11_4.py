#버전1
'''
num_dict = {'일':'one', '이':'two', '삼':'three', '사':'four','오':'five','육':'six','칠':'seven','팔':'eight','구':'nine','십':'ten',
            'one':'일', 'two':'이', 'three':'삼', 'four':'사','five':'오','six':'육','seven':'칠','eight':'팔','nine':'구','ten':'십'}

while True:
    word = input('검색할 단어를 입력하세요(종료시 \'0\' 입력): ')
    if word == '0':             #종료
        break

    if word in num_dict.keys():   #사전에 있을 때
        print(num_dict[word])
    else:                       #잘못 입력한 경우
        print("잘못 입력하셨습니다")

'''

#버전2
dicKor = { '일':'one', '이':'two', '삼':'three', '사':'four','오':'five','육':'six','칠':'seven','팔':'eight','구':'nine','십':'ten' }
dicEng = { 'one':'일', 'two':'이', 'three':'삼', 'four':'사','five':'오','six':'육','seven':'칠','eight':'팔','nine':'구','ten':'십' }


while True:
    word = input('검색할 단어를 입력하세요(종료시 \'0\' 입력): ')
    if word == '0':             #종료
        break

    if word in dicKor.keys():   #한영사전에 있을 때
        print(dicKor[word])
    elif word in dicEng.keys(): #영한사전에 있을 때
        print(dicEng[word])
    else:                       #잘못 입력한 경우
        print("잘못 입력하셨습니다")
