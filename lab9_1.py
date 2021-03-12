#abs() 사용 전 
def func1 (x,y):
    if x-y > 0:
        return x-y
    else:
        return y-x

#abs() 사용 후
def func2 (x,y):
    return abs(x-y)


help(func1)
help(func2)

