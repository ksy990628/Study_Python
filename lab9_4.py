oct ="01234567"

def ConvertToOct(x):
    q = x // 8
    r = x % 8

    if(q==0):
        return oct[r]
    else:
        return ConvertToOct(q) + oct[r]


num = int(input('정수를 입력하세요 :'))
print(ConvertToOct(num))
