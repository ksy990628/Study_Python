#문자열 역순 출력

#방법 1
str = input('문자열을 입력하세요: ')  #문자열 입력

str_list = list(str)    #문자열 리스트형으로 저장
str_list.reverse()      #리스트 역순 정렬
result = str_list       #리스트 역순 정렬된 것을 result에 저장

for i in result:
    print(i, end="")           #출력
print('\n')

#방법 2
str = input("문자열을 입력하세요: ")   #문자열 입력

tempList = list(str)    #문자열 리스트형으로 저장
tempList.reverse()      #리스트 역순 정렬
result = ''

for char in tempList :
    result += char      #리스트 역순 정렬된 것을 result에 저장

print(result)           #출력


#방법3
str = input('문자열을 입력하시오: ')
list = []

for i in range(len(str)):
    list.append(str[i])

list.reverse()

result = ''

for j in range(len(str)):
    result += list[j]


print(result)
