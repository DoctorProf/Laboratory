from random import randint
a =[]
M = int(input('Введите M-'))
N = int(input('Введите N-'))
for i in range(M):
		a.append([])
		for j in range(N):
			a[i].append(randint(1, 3))
		print(a[i])
print('\n')
def swap_columns(a, i, j):
    for r in range(M):
        a[r][i],a[r][j] = a[r][j],a[r][i] 
        print(a[r])

swap_columns(a,0,2)