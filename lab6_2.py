for x in range(0,5):
    for y in range(0,x+1,1):
        print("*", end="")
    print()


for x in range(0,5):
    stars = ' '
    for y in range(0,x+1):
        stars = stars + '*'
    print(stars)


x = 1
while x <= 5:
    stars = "*"
    blank = " "
    print(stars*x,blank*(5-x))
    x += 1
