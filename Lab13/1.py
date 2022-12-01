from random import randint
m =[]
M = int(input('Введите M-'))
N = int(input('Введите N-'))
for i in range(M):
		m.append([])
		for j in range(N):
			m[i].append(randint(1, 3))
for i in range(1, M):
	for j in range(M-1, N-i, -1):
			m[i-1][j-1] =0
for i in m:
	print(i)