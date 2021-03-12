file = open('lab12_3_phone.txt', 'r')
phone_list = []

for line in file :
    phone_list.append(line)

file.close()

phone_list.sort()

file = open('sorted_phone.txt', 'w')
for num in phone_list :
    file.write(str(num))

file.close()    
