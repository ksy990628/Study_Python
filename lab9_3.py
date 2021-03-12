hex ="0123456789abcdef"

def ConvertToHex(x):
    q = x // 16
    r = x % 16

    if(q==0):
        return hex[r]
    else:
        return ConvertToHex(q) + hex[r]


num = int(input('정수를 입력하세요 :'))
print(ConvertToHex(num))
