pH = float(input('pH 농도를 입력하시오: '))
if pH > 7.0:
    print('염기성')
else:
    if pH < 7.0:
        print('산성')
        if pH < 3.0:
            print('주의! 강산성')
    else:
        print('중성')


'''
pH = float(input('pH 농도를 입력하시오: '))
if pH > 7.0:
    print('염기성')
elif pH < 7.0:
    print('산성')
        if pH < 3.0:
            print('주의! 강산성')
else:
    print('중성')

'''
