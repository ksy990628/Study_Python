morse = { 'A':'._', 'B':'_...', 'C':'_._.', 'D':'_..', 'E':'.', 'F':'.._.',
'G':'__.', 'H':'....', 'I':'..', 'J':'.___', 'K':'_._', 'L':'._..',
'M':'__', 'N':'_.', 'O':'___', 'P':'.__.', 'Q':'__._', 'R':'._.',
'S':'...', 'T':'_', 'U':'.._', 'V':'..._', 'W':'.__', 'X':'_.._',
'Y':'_.__', 'Z':'__..' }


def print_morse(s) : # 문자열 s에 대한 모스 부호를 출력하는 함수
    result = ''
    s = s.upper() # 입력된 문자열을 대문자로 변경

    for char in s : # 문자열의 각 문자에 대해 모스 부호로 변경
        if char == ' ' :
            continue # 공백일 경우 건너뛰기
        #문자인 경우 해당하는 모스 부호로 출력, 해당하는 모스 부호 없을 시 공백
        result += morse.get(char,'')  
        #result += morse[char] # 문자인 경우 해당하는 모스 부호로 변경

    return result # 결과 반환
