with open('test1.txt','r') as line:
    lis=[i.rstrip()  for i in line .read() if i.rstrip()]
for i in sorted(set(lis)):
    print(i,lis.count(i))
line.close()
