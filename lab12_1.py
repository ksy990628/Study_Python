max_score = 0
max_name =''

with open('lab12_1.txt','r',encoding="UTF8") as file:
    for line in file:
        current = line.split()
        if int(current[1]) > max_score:
            max_score = int(current[1])
            max_name = current[0]

print('가장 높은 성적을 받은 학생: ',max_name)
print('가장 높은 성적: ',max_score)
