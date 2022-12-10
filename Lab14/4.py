from random import randint
m = []
M = int(input('Введите M-'))
N = int(input('Введите N-'))
for i in range(M):
    m.append([])
    for j in range(N):
        m[i].append(randint(1,5))
    print(m[i])
print('\n')
for k in range(M):
    for i in range(M):
        for j in range(N - 1):
            if m[i][j] > m[i][j+1]:
                m[i][j] , m[i][j+1] = m[i][j+1], m[i][j]
for i in m:
    print(i)