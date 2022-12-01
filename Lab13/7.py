from random import randint
m =[]
sumDiag = 0
sumPod = 0
M = int(input('Введите M-'))
for i in range(M):
		m.append([])
		for j in range(M):
			m[i].append(randint(1, 5))
		print(m[i])
for i in range(M):
    for j in range(i): 
        sumPod += m[i][j]
for i in range(M):
    for j in range(M): 
        if i == j:
            sumDiag+=m[i][j]
print('Сумма элементов  под диагогналью', sumPod)
print('Сумма элементов диагогнали', sumDiag)