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
    for i in range(M-1):
        if m[i][0] > m[i+1][0]:
            for j in range(N):
                m[i][j], m[i+1][j] = m[i+1][j],m[i][j]
for i in m:
    print(i)