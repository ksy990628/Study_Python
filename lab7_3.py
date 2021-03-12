elements = ['Li','Na','K','F','CI']

value = input("탐색할 원소를 입력하세요: ")

for i in range(len(elements)-1,-1,-1):
    if elements[i] == value:
        print('%d번째에 있습니다' %i)
        break

if i == 0 and elements[i] != value:
         print('탐색 실패')
