f = open("test1.txt",'r')
sum = 0
lst = f.readlines()
for i in lst:
    sum += int(i)
sr = sum/len(lst)
print('Среднее арифметическое', sr)
f.close()
f = open("test2.txt",'w')
f.writelines(str(sr))
f.close()