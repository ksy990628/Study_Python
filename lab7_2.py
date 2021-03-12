elements = ['Li','Na','K','F','CI']

i = len(elements)-1

value = input("탐색할 원소를 입력하세요: ")
while i >= 0 and elements[i] != value:
	i = i-1
	
if i < 0 :
    print('탐색 실패')
else:
    print('%d번째에 있습니다' %i)
