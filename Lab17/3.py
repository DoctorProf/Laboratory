f = open("test1.txt",'r')
lst = f.readlines()
for k in lst:
    for i in range(len(lst)-1):
        if int(lst[i]) > int(lst[i+1]):
            lst[i], lst[i+1] = lst[i +1] , lst[i]
print(lst)
f.close()
f = open("test2.txt",'r')
lst1 = f.readlines()
for k in lst1:
    for i in range(len(lst1)-1):
        if int(lst1[i]) > int(lst1[i+1]):
            lst1[i], lst1[i+1] = lst1[i +1] , lst1[i]
print(lst1)
f.close()
f = open("test3.txt",'w')
f.writelines(lst + lst1)
f.close()