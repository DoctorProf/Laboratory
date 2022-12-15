word = ['оn', 'in' , 'at','near' ,'over','under' ,'between' ,'among' ,'behind' ,'асrоss' ,'in front оf','through']

with open('test1.txt','r') as line:
    lis=[i.rstrip()  for i in line .readlines() if i.rstrip()]
    
print('Первый текст')

for i in sorted(set(lis)):
    for k in word:
        if i == k:
            print(i,lis.count(i))
line.close()

with open('test2.txt','r') as line2:
    lis1=[i.rstrip()  for i in line2 .readlines() if i.rstrip()]
    
print('Второй текст')

for i in sorted(set(lis1)):
    for k in word:
        if i == k:
            print(1)
            print(i,lis1.count(i))
line2.close()

