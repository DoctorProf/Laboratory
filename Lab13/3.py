from random import randint
m =[]
M = int(input('Введите M-'))
N = int(input('Введите N-'))
for i in range(M):
		m.append([])
		for j in range(N):
			m[i].append(i+j+1)
for i in m:
	print(i)