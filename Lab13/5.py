from random import randint
m =[]
sum = 0
M = int(input('Введите M-'))
N = int(input('Введите N-'))
for i in range(M):
	m.append([])
	for j in range(N):
		m[i].append(randint(0, 1))
		sum+=m[i][j]
	print(m[i])
print('Сумма=',sum)