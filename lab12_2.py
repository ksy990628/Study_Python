with open('lab12_2.txt','w+') as file:
    file.write('The color is brown')
    file.seek(13)
    file.write("green")
    file.seek(0)
    result = file.read()

print(result)

#    for line in file:
#        print(line.strip())

