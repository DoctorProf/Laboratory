from random import randint
m =[]
M = int(input('Введите M-'))
for i in range(M):
		m.append([])
		for j in range(M):
			m[i].append(randint(1, 3))

for i in range(M):
    for j in range(i + 1, M): 
        m[i][j] = 0
    for k in range(i + 1):
        m[i][k] = 1

for i in m:
	print(i)