f = open("test1.txt",'r')
lst = f.readlines()
for k in lst:
    for i in range(len(lst)-1):
        if int(lst[i]) > int(lst[i+1]):
            lst[i], lst[i+1] = lst[i +1] , lst[i]
print(lst)
f.close()
f = open("test1.txt",'w')
f.writelines(lst)
f.close()