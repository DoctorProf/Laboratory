f = open("test1.txt",'r')
sum = 0
lst = f.readlines()
for i in lst:
    sum += int(i)
print('Сумма', sum)
f.close()