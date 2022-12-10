f = open("test1.txt",'r')
itog = []
sp =[]
lst = f.readlines()
for i in range(len(lst)):
        sp.append(lst[i].split(" "))
for i in range(len(lst)):
    for j in range(len(sp)):
        if sp[i][j][0].upper() == 'A':
            itog.append(lst[i])
f.close()
f = open("test2.txt",'w')
f.writelines(itog)
f.close()