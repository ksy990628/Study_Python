phone_list = []

with open('lab12_3_phone.txt','r') as file:
    for line in file:
        phone_list.append(line.strip())
    phone_list.sort()

print(phone_list)


with open('lab12_3.txt','w') as file:
    for i in phone_list:
        file.write(i+"\n")

        
