from random import randint
import numpy
m1=[]
for i in range(5):
	m1.append([])
	for j in range(3): m1[i].append(randint(1, 3))

m2=[]
for i in range(3):
	m2.append([])
	for j in range(2):
		m2[i].append(randint(1, 3))

resultM = numpy.dot(m1, m2)
for i in resultM:
    print(i)