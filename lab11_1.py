#두 집합의 합집합, 교집합, 차집합 및 대칭차집합 구하기

A = { 'a', 'n', 'e', 't', 'x', 'y', 'n', 'w' }
B = { 'p', 'y', 't', 'h', 'o', 'n' }


#set 함수 이용
print('SET 함수\n')
print('합집합: ',A.union(B))
print('교집합: ',A.intersection(B))
print('차집합: ',A.difference(B))
print('차집합: ',B.difference(A))
print('대칭차집합: ',A.symmetric_difference(B))


print('\n\n\n')


#연산자 이용
print('연산자\n')
print('합집합: ',A | B)
print('교집합: ',A & B)
print('차집합: ',A - B)
print('차집합: ',B - A)
print('대칭차집합: ',A ^ B)
