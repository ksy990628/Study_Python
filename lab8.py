# 문제 1
# Factorial 계산
# Factorial은 1부터 n까지의 정수를 모두 곱하는 것
# n! = 1 * 2 * 3 * … * n

i = 1 # 반복문의 조건을 따지기 위한 변수
result = 1 # 팩토리얼 계산 결과를 저장하기 위한 변수

n = int(input('팩토리얼을 계산할 숫자를 입력하세요'))
while i <= n:
    result *= i
    i += 1

print(result)


# 문제 2
대만 = 21
대한민국 = 47
몽골 = 3
홍콩 = 7
중국 = 23
북한 = 1295
total = 대만 + 대한민국 + 몽골 + 홍콩 + 중국 + 북한

print("모든 나라들의 인구수 총합은 %d 백만명입니다."%(total))





#문제 3
C = float(input('섭씨 온도를 입력하세요: '))
F = C * (9 / 5) + 32

print("섭씨\t화씨\n%.1f\t%f"%(C, F))

